# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
"""
Network-based computation of operations & data.

The execution of network *operations* is splitted in 2 phases:

COMPILE:
    prune unsatisfied nodes, sort dag topologically & solve it, and
    derive the *execution steps* (see below) based on the given *inputs*
    and asked *outputs*.

EXECUTE:
    sequential or parallel invocation of the underlying functions
    of the operations with arguments from the ``solution``.

Computations are based on 5 data-structures:

:attr:`Network.graph`
    A ``networkx`` graph (yet a DAG) containing interchanging layers of
    :class:`Operation` and :class:`_DataNode` nodes.
    They are layed out and connected by repeated calls of
    :meth:`~Network.add_OP`.

    The computation starts with :meth:`~Network.prune()` extracting
    a *DAG subgraph* by *pruning* its nodes based on given inputs and
    requested outputs in :meth:`~Network.compute()`.

:attr:`ExecutionPlan.dag`
    An directed-acyclic-graph containing the *pruned* nodes as build by
    :meth:`~Network.prune()`. This pruned subgraph is used to decide
    the :attr:`ExecutionPlan.steps` (below).
    The containing :class:`ExecutionPlan.steps` instance is cached
    in :attr:`_cached_plans` across runs with inputs/outputs as key.

:attr:`ExecutionPlan.steps`
    It is the list of the operation-nodes only
    from the dag (above), topologically sorted, and interspersed with
    *instruction steps* needed to complete the run.
    It is built by :meth:`~Network._build_execution_steps()` based on
    the subgraph dag extracted above.
    The containing :class:`ExecutionPlan.steps` instance is cached
    in :attr:`_cached_plans` across runs with inputs/outputs as key.

    The *instructions* items achieve the following:

    - :class:`_EvictInstruction`: evicts items from `solution` as soon as
        they are not needed further down the dag, to reduce memory footprint
        while computing.

    - :class:`_PinInstruction`: avoid overwritting any given intermediate
        inputs, and still allow their providing operations to run
        (because they are needed for their other outputs).

:var solution:
    a local-var in :meth:`~Network.compute()`, initialized on each run
    to hold the values of the given inputs, generated (intermediate) data,
    and output values.
    It is returned as is if no specific outputs requested;  no data-eviction
    happens then.

:arg overwrites:
    The optional argument given to :meth:`~Network.compute()` to colect the
    intermediate *calculated* values that are overwritten by intermediate
    (aka "pinned") input-values.
"""
import logging
import re
import sys
import time
from collections import abc, defaultdict, namedtuple
from contextvars import ContextVar
from multiprocessing.dummy import Pool
from typing import Collection, Iterable, List, Optional, Tuple

import networkx as nx
from boltons.setutils import IndexedSet as iset
from networkx import DiGraph

from .base import Plotter, aslist, astuple, jetsam
from .modifiers import optional, sideffect
from .op import Operation

log = logging.getLogger(__name__)


#: Global configurations for all (nested) networks in a computaion run.
_execution_configs: ContextVar[dict] = ContextVar(
    "execution_configs",
    default={"execution_pool": Pool(7), "abort": False, "skip_evictions": False},
)


class AbortedException(Exception):
    """Raised from the Network code when :func:`abort_run()` is called."""


def abort_run():
    _execution_configs.get()["abort"] = True


def _reset_abort():
    _execution_configs.get()["abort"] = False


def is_abort():
    return _execution_configs.get()["abort"]


def set_evictions_skipped(skipped):
    _execution_configs.get()["skip_evictions"] = skipped


def is_skip_evictions():
    return _execution_configs.get()["skip_evictions"]


class _DataNode(str):
    """
    Dag node naming a data-value produced or required by an operation.
    """

    __slots__ = ()  # avoid __dict__ on instances

    def __repr__(self):
        return 'DataNode("%s")' % self


class _EvictInstruction(str):
    """
    Execution step to evict a computed value from the `solution`.

    It's a step in :attr:`ExecutionPlan.steps` for the data-node `str` that
    frees its data-value from `solution` after it is no longer needed,
    to reduce memory footprint while computing the graph.
    """

    __slots__ = ()  # avoid __dict__ on instances

    def __repr__(self):
        return 'EvictInstruction("%s")' % self


class _PinInstruction(str):
    """
    Execution step to overwrite a computed value in the `solution` from the inputs,

    and to store the computed one in the ``overwrites`` instead
    (both `solution` & ``overwrites`` are local-vars in :meth:`~Network.compute()`).

    It's a step in :attr:`ExecutionPlan.steps` for the data-node `str` that
    ensures the corresponding intermediate input-value is not overwritten when
    its providing function(s) could not be pruned, because their other outputs
    are needed elesewhere.
    """

    __slots__ = ()  # avoid __dict__ on instances

    def __repr__(self):
        return 'PinInstruction("%s")' % self


# TODO: maybe class Solution(object):
#     values = {}
#     overwrites = None


def _yield_datanodes(graph):
    return (n for n in graph if isinstance(n, _DataNode))


def _optionalized(graph, data):
    """Retain optionality of a `data` node based on all `needs` edges."""
    all_optionals = all(e[2] for e in graph.out_edges(data, "optional", False))
    sideffector = graph.nodes(data="sideffect")
    return (
        optional(data)
        if all_optionals
        # Nodes are _DataNode instances, not `optional` or `sideffect`
        # TODO: Unify _DataNode + modifiers to avoid ugly hack `net.collect_requirements()`.
        else sideffect(re.match(r"sideffect\((.*)\)", data).group(1))
        if sideffector[data]
        else str(data)  # un-optionalize
    )


def collect_requirements(graph) -> Tuple[iset, iset]:
    """Collect and split datanodes all `graph` ops in needs/provides."""
    operations = [op for op in graph if isinstance(op, Operation)]
    provides = iset(p for op in operations for p in op.provides)
    needs = (
        iset(_optionalized(graph, n) for op in operations for n in op.needs) - provides
    )
    # TODO: Unify _DataNode + modifiers to avoid ugly hack `net.collect_requirements()`.
    provides = iset(str(n) if not isinstance(n, sideffect) else n for n in provides)
    return needs, provides


class ExecutionPlan(
    namedtuple("_ExePlan", "net needs provides dag broken_edges steps evict"), Plotter
):
    """
    The result of the network's compilation phase.

    Note the execution plan's attributes are on purpose immutable tuples.

    :ivar net:
        The parent :class:`Network`
    :ivar needs:
        A tuple with the input names needed to exist in order to produce all `provides`.
    :ivar provides:
        A tuple with the outputs names produces when all `inputs` are given.
    :ivar dag:
        The regular (not broken) *pruned* subgraph of net-graph.
    :ivar broken_edges:
        Tuple of broken incoming edges to given data.
    :ivar steps:
        The tuple of operation-nodes & *instructions* needed to evaluate
        the given inputs & asked outputs, free memory and avoid overwritting
        any given intermediate inputs.
    :ivar evict:
        when false, keep all inputs & outputs, and skip prefect-evictions check.
    """

    @property
    def broken_dag(self):
        return nx.restricted_view(self.dag, nodes=(), edges=self.broken_edges)

    def _build_pydot(self, **kws):
        from .plot import build_pydot

        clusters = None
        if self.dag.nodes != self.net.graph.nodes:
            clusters = {n: "after prunning" for n in self.dag.nodes}
        mykws = {
            "graph": self.net.graph,
            "steps": self.steps,
            "inputs": self.needs,
            "outputs": self.provides,
            "edge_props": {
                e: {"color": "wheat", "penwidth": 2} for e in self.broken_edges
            },
            "clusters": clusters,
        }
        mykws.update(kws)

        return build_pydot(**mykws)

    def __repr__(self):
        steps = ["\n  +--%s" % s for s in self.steps]
        return "ExecutionPlan(needs=%s, provides=%s, steps:%s)" % (
            aslist(self.needs, "needs"),
            aslist(self.provides, "provides"),
            "".join(steps),
        )

    def validate(
        self, inputs: Optional[abc.Collection], outputs: Optional[abc.Collection]
    ):
        """
        Scream on invalid inputs, outputs or no operations in graph.

        :raises ValueError:
            - If given `inputs` mismatched :attr:`needs`, with msg:

                *Plan needs more inputs...*
            - If `outputs` asked cannot be produced by the :attr:`dag`, with msg:

                *Impossible outputs...*

            - If cannot produce any `outputs` from the given `inputs`, with msg:

                *Unsolvable graph: ...*
        """
        if not self.dag:
            raise ValueError(f"Unsolvable graph:\n  {self}")

        # Check plan<-->inputs mismatch.
        #
        missing = iset(self.needs) - set(inputs)
        if missing:
            raise ValueError(
                f"Plan needs more inputs: {list(missing)}"
                f"\n  given inputs: {list(inputs)}\n  {self}"
            )

        if outputs:
            unknown = (
                iset(astuple(outputs, "outputs", allowed_types=abc.Sequence))
                - self.provides
            )
            if unknown:
                raise ValueError(
                    f"Impossible outputs: {list(unknown)}\n for graph: {self}"
                    f"\n  {self}"
                )

    def _pin_data_in_solution(self, value_name, solution, inputs, overwrites):
        value_name = str(value_name)
        if overwrites is not None:
            overwrites[value_name] = solution[value_name]
        solution[value_name] = inputs[value_name]

    def _check_if_aborted(self, executed):
        if is_abort():
            # Restore `abort` flag for next run.
            _reset_abort()
            raise AbortedException({s: s in executed for s in self.steps})

    def _call_operation(self, op, solution):
        # Although `plan` have added to jetsam in `compute()``,
        # add it again, in case compile()/execute is called separately.
        try:
            return op.compute(solution)
        except Exception as ex:
            jetsam(ex, locals(), plan="self")

    def _execute_thread_pool_barrier_method(self, solution, overwrites, executed):
        """
        This method runs the graph using a parallel pool of thread executors.
        You may achieve lower total latency if your graph is sufficiently
        sub divided into operations using this method.

        :param solution:
            must contain the input values only, gets modified
        """
        # Keep original inputs for pinning.
        pinned_values = {
            n: solution[n] for n in self.steps if isinstance(n, _PinInstruction)
        }

        pool = _execution_configs.get()["execution_pool"]

        # with each loop iteration, we determine a set of operations that can be
        # scheduled, then schedule them onto a thread pool, then collect their
        # results onto a memory solution for use upon the next iteration.
        while True:
            self._check_if_aborted(executed)

            # the upnext list contains a list of operations for scheduling
            # in the current round of scheduling
            upnext = []
            for node in self.steps:
                ## Determines if a Operation is ready to be scheduled for execution
                #  based on what has already been executed.
                if (
                    isinstance(node, Operation)
                    and node not in executed
                    #  Use `broken_dag` to allow executing operations from given inputs
                    #  regardless of whether their producers have yet to re-calc them.
                    and set(
                        n
                        for n in nx.ancestors(self.broken_dag, node)
                        if isinstance(n, Operation)
                    ).issubset(executed)
                ):
                    upnext.append(node)
                elif isinstance(node, _EvictInstruction):
                    # Only evict if all successors for the data node
                    # have been executed.
                    if (
                        # An optional need may not have a value in the solution.
                        node in solution
                        and (
                            # The 2nd eviction branch for unused provides.
                            node not in self.dag.nodes
                            # Scan node's successors in `broken_dag`, not to block
                            # an op waiting for calced data already given as input.
                            or set(self.broken_dag.successors(node)).issubset(executed)
                        )
                    ):
                        log.debug("removing data '%s' from solution.", node)
                        del solution[node]
                elif isinstance(node, _PinInstruction):
                    # Always and repeatedely pin the value, even if not all
                    # providers of the data have executed.
                    # An optional need may not have a value in the solution.
                    if node in solution:
                        self._pin_data_in_solution(
                            node, solution, pinned_values, overwrites
                        )

            # stop if no nodes left to schedule, exit out of the loop
            if not upnext:
                break

            done_iterator = pool.imap_unordered(
                (lambda op: (op, self._call_operation(op, solution))), upnext
            )

            for op, result in done_iterator:
                solution.update(result)
                executed.add(op)

    def _execute_sequential_method(self, solution, overwrites, executed):
        """
        This method runs the graph one operation at a time in a single thread

        :param solution:
            must contain the input values only, gets modified
        """
        # Keep original inputs for pinning.
        pinned_values = {
            n: solution[n] for n in self.steps if isinstance(n, _PinInstruction)
        }

        self.times = {}
        for step in self.steps:
            self._check_if_aborted(executed)

            if isinstance(step, Operation):

                log.debug("%sexecuting step: %s", "-" * 32, step.name)

                # time execution...
                t0 = time.time()

                # compute layer outputs
                layer_outputs = self._call_operation(step, solution)

                # add outputs to solution
                solution.update(layer_outputs)
                executed.add(step)

                # record execution time
                t_complete = round(time.time() - t0, 5)
                self.times[step.name] = t_complete
                log.debug("step completion time: %s", t_complete)

            elif isinstance(step, _EvictInstruction):
                # Cache value may be missing if it is optional.
                if step in solution:
                    log.debug("removing data '%s' from solution.", step)
                    del solution[step]

            elif isinstance(step, _PinInstruction):
                self._pin_data_in_solution(step, solution, pinned_values, overwrites)
            else:
                raise AssertionError("Unrecognized instruction.%r" % step)

    def execute(self, named_inputs, outputs=None, *, overwrites=None, method=None):
        """
        :param named_inputs:
            A maping of names --> values that must contain at least
            the compulsory inputs that were specified when the plan was built
            (but cannot enforce that!).
            Cloned, not modified.
        :param outputs:
            If not None, they are just checked if possible, based on :attr:`provides`,
            and scream if not.
        :param overwrites:
            (optional) a mutable dict to collect calculated-but-discarded values
            because they were "pinned" by input vaules.
            If missing, the overwrites values are simply discarded.

        :raises ValueError:
            - If given `inputs` mismatched `plan.needs`, with msg:

                *Plan needs more inputs...*
            - If `outputs` asked cannot be produced by the `graph`, with msg:

                *Impossible outputs...*

            - If cannot produce any `outputs` from the given `inputs`, with msg:

                *Unsolvable graph: ...*
        """
        try:
            self.validate(named_inputs, outputs)

            # choose a method of execution
            executor = (
                self._execute_thread_pool_barrier_method
                if method == "parallel"
                else self._execute_sequential_method
            )

            # If certain outputs asked, put relevant-only inputs in solution,
            # otherwise, keep'em all.
            # Note: clone and keep orignal inputs in solution intact
            solution = (
                {k: v for k, v in named_inputs.items() if k in self.dag.nodes}
                if self.evict
                else named_inputs.copy()
            )
            executed = set()
            executor(solution, overwrites, executed)

            # Validate eviction was perfect
            assert (
                not self.evict
                or is_skip_evictions()
                # It is a proper subset when not all outputs calculated.
                or set(solution).issubset(self.provides)
            ), f"Evictions left more data{list(iset(solution) - set(self.provides))} than {self}!"

            return solution
        except Exception as ex:
            jetsam(ex, locals(), "solution", "executed")


class Network(Plotter):
    """
    Assemble operations & data into a directed-acyclic-graph (DAG) to run them.

    :ivar needs:
        the "base", all data-nodes that are not produced by some operation
    :ivar provides:
        the "base", all data-nodes produced by some operation
    """

    def __init__(self, *operations):
        ## Check for duplicate, operations can only append  once.
        #
        uniques = set(operations)
        if len(operations) != len(uniques):
            dupes = list(operations)
            for i in uniques:
                dupes.remove(i)
            raise ValueError(f"Operations may only be added once, dupes: {list(dupes)}")

        # directed graph of layer instances and data-names defining the net.
        graph = self.graph = DiGraph()
        for op in operations:
            self._append_operation(graph, op)
        self.needs, self.provides = collect_requirements(self.graph)

        # this holds the timing information for each layer
        self.times = {}

        #: Speed up :meth:`compile()` call and avoid a multithreading issue(?)
        #: that is occuring when accessing the dag in networkx.
        self._cached_plans = {}

    def __repr__(self):
        steps = ["\n  +--%s" % s for s in self.graph.nodes]
        return "Network(%s)" % "".join(steps)

    def _build_pydot(self, **kws):
        from .plot import build_pydot

        kws.setdefault("graph", self.graph)

        return build_pydot(**kws)

    def _append_operation(self, graph, operation: Operation):
        """
        Adds the given operation and its data requirements to the network graph.

        - Invoked dyuring constructor only (immutability).
        - Identities are based on the name of the operation, the names of the operation's needs,
          and the names of the data it provides.

        :param graph:
            the `networkx` graph to append to
        :param operation:
            operation instance to append
        """
        # add nodes and edges to graph describing the data needs for this layer
        for n in operation.needs:
            kw = {}
            if isinstance(n, optional):
                kw["optional"] = True
            if isinstance(n, sideffect):
                kw["sideffect"] = True
                graph.add_node(_DataNode(n), sideffect=True)
            graph.add_edge(_DataNode(n), operation, **kw)

        # add nodes and edges to graph describing what this layer provides
        for n in operation.provides:
            kw = {}
            if isinstance(n, sideffect):
                kw["sideffect"] = True
                graph.add_node(_DataNode(n), sideffect=True)
            graph.add_edge(operation, _DataNode(n), **kw)

    def _collect_unsatisfied_operations(self, dag, inputs: Collection):
        """
        Traverse topologically sorted dag to collect un-satisfied operations.

        Unsatisfied operations are those suffering from ANY of the following:

        - They are missing at least one compulsory need-input.
          Since the dag is ordered, as soon as we're on an operation,
          all its needs have been accounted, so we can get its satisfaction.

        - Their provided outputs are not linked to any data in the dag.
          An operation might not have any output link when :meth:`prune()`
          has broken them, due to given intermediate inputs.

        :param dag:
            a graph with broken edges those arriving to existing inputs
        :param inputs:
            an iterable of the names of the input values
        :return:
            a list of unsatisfied operations to prune

        """
        # To collect data that will be produced.
        ok_data = set(inputs)
        # To colect the map of operations --> satisfied-needs.
        op_satisfaction = defaultdict(set)
        # To collect the operations to drop.
        unsatisfied = []
        for node in nx.topological_sort(dag):
            if isinstance(node, Operation):
                if not dag.adj[node]:
                    # Prune operations that ended up providing no output.
                    unsatisfied.append(node)
                else:
                    # It's ok not to dig into edge-data("optional") here,
                    # we care about all needs, including broken ones.
                    real_needs = set(
                        n for n in node.needs if not isinstance(n, optional)
                    )
                    if real_needs.issubset(op_satisfaction[node]):
                        # We have a satisfied operation; mark its output-data
                        # as ok.
                        ok_data.update(dag.adj[node])
                    else:
                        # Prune operations with partial inputs.
                        unsatisfied.append(node)
            elif isinstance(node, (_DataNode, str)):  # `str` are givens
                if node in ok_data:
                    # mark satisfied-needs on all future operations
                    for future_op in dag.adj[node]:
                        op_satisfaction[future_op].add(node)
            else:
                raise AssertionError("Unrecognized network graph node %r" % node)

        return unsatisfied

    def prune(
        self, inputs: Optional[Collection], outputs: Optional[Collection]
    ) -> Tuple[nx.DiGraph, Collection, Collection, Collection]:
        """
        Determines what graph steps need to run to get to the requested
        outputs from the provided inputs:
        - Eliminate steps that are not on a path arriving to requested outputs;
        - Eliminate unsatisfied operations: partial inputs or no outputs needed;
        - consolidate the list of needs & provides.

        :param inputs:
            The names of all given inputs.

        :param outputs:
            The desired output names.  This can also be ``None``, in which
            case the necessary steps are all graph nodes that are reachable
            from the provided inputs.

        :return:
            a 4-tuple with the *pruned_dag*, the out-edges of the inputs,
            and needs/provides resolved.

        :raises ValueError:
            - if `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*
        """
        # TODO: break cycles here.
        dag = self.graph

        if inputs is None and outputs is None:
            inputs, outputs = self.needs, self.provides
        else:
            if inputs is None:  # means outputs are non-null ...
                # Consider "preliminary" `inputs` any non-output node.
                inputs = iset(_yield_datanodes(dag)) - outputs
            else:
                # Ignore `inputs` not in the graph.
                inputs = iset(inputs) & dag.nodes

            ## Scream on unknown `outputs`.
            #
            if outputs:
                unknown_outputs = iset(outputs) - dag.nodes
                if unknown_outputs:
                    raise ValueError(
                        f"Unknown output nodes: {list(unknown_outputs)}\n  {self}"
                    )

        assert isinstance(inputs, abc.Collection)
        assert outputs is None or isinstance(outputs, abc.Collection)

        broken_dag = dag.copy()  # preserve net's graph
        broken_edges = set()  # unordered, not iterated

        # Break the incoming edges to all given inputs.
        #
        # Nodes producing any given intermediate inputs are unecessary
        # (unless they are also used elsewhere).
        # To discover which ones to prune, we break their incoming edges
        # and they will drop out while collecting ancestors from the outputs.
        #
        if inputs:
            for given in inputs:
                broken_edges.update(broken_dag.in_edges(given))
            broken_dag.remove_edges_from(broken_edges)

        # Drop stray input values and operations (if any).
        if outputs is not None:
            # If caller requested specific outputs, we can prune any
            # unrelated nodes further up the dag.
            ending_in_outputs = set()
            for output_name in outputs:
                ending_in_outputs.add(_DataNode(output_name))
                ending_in_outputs.update(nx.ancestors(dag, output_name))
            broken_dag = broken_dag.subgraph(ending_in_outputs)

        # Prune unsatisfied operations (those with partial inputs or no outputs).
        unsatisfied = self._collect_unsatisfied_operations(broken_dag, inputs)
        # Clone it, to modify it.
        pruned_dag = dag.subgraph(broken_dag.nodes - unsatisfied).copy()

        pruned_dag.remove_nodes_from(list(nx.isolates(pruned_dag)))

        inputs = iset(_optionalized(pruned_dag, n) for n in inputs if n in pruned_dag)
        if outputs is None:
            outputs = iset(
                n for n in self.provides if n not in inputs and n in pruned_dag
            )

        assert all(_yield_datanodes(pruned_dag)), pruned_dag
        assert inputs is not None or isinstance(inputs, abc.Collection)
        assert outputs is not None or isinstance(outputs, abc.Collection)

        return pruned_dag, broken_edges, tuple(inputs), tuple(outputs)

    def _build_execution_steps(
        self, pruned_dag, inputs: Optional[Collection], outputs: Optional[Collection]
    ) -> List:
        """
        Create the list of operation-nodes & *instructions* evaluating all

        operations & instructions needed a) to free memory and b) avoid
        overwritting given intermediate inputs.

        :param pruned_dag:
            The original dag, pruned; not broken.
        :param outputs:
            outp-names to decide whether to add (and which) evict-instructions

        Instances of :class:`_EvictInstructions` are inserted in `steps` between
        operation nodes to reduce the memory footprint of solutions while
        the computation is running.
        An evict-instruction is inserted whenever a *need* is not used
        by any other *operation* further down the DAG.
        """

        steps = []

        def add_step_once(step):
            # For functions with repeated needs, like ['a', 'a'].
            if steps and step == steps[-1] and type(step) == type(steps[-1]):
                log.warning("Skipped dupe step %s in position %i.", step, len(steps))
            else:
                steps.append(step)

        # create an execution order such that each layer's needs are provided.
        ordered_nodes = iset(nx.topological_sort(pruned_dag))

        # Add Operations evaluation steps, and instructions to free and "pin"
        # data.
        for i, node in enumerate(ordered_nodes):

            if isinstance(node, _DataNode):
                ## Add PIN-instruction if data node matches an input.
                #
                #  + Links MUST NOT be broken, check if provided depends on them.
                #  + Pin decision can happen when visiting this data-node
                #    because all operations producing it have run,
                #    and none needing it has begun running.
                #  + Pin happens before any eviction-instruction - actually
                #    an operation execution must seprate them.
                #
                if (
                    node in inputs
                    # Don't pin sideffect nodes.
                    and "sideffect" not in pruned_dag.nodes[node]
                    # Pin only if non-prune operation generating it.
                    and pruned_dag.pred[node]
                ):
                    add_step_once(_PinInstruction(node))

            elif isinstance(node, Operation):
                steps.append(node)

                # NO EVICTIONS when no specific outputs asked.
                if not outputs or is_skip_evictions():
                    continue

                # Add EVICT (1) for operation's needs.
                #
                # Broken links are irrelevant because they are preds of data (provides),
                # but here we scan for preds of the operation (needs).
                #
                for need in pruned_dag.pred[node]:
                    # Do not evict asked outputs or sideffects.
                    if need in outputs:
                        continue

                    # A needed-data of this operation may be evicted if
                    # no future Operations needs it.
                    #
                    for future_node in ordered_nodes[i + 1 :]:
                        if (
                            isinstance(future_node, Operation)
                            and need in pruned_dag.pred[future_node]
                        ):
                            break
                    else:
                        add_step_once(_EvictInstruction(need))

                # Add EVICT (2) for unused operation's provides.
                #
                # A provided-data is evicted if no future operation needs it
                # (and is not an asked output).
                # It MUST use the broken dag, not to evict data
                # that will be pinned, but to populate overwrites with them.
                #
                # .. image:: doc/source/images/unpruned_useless_provides.svg
                #
                for provide in node.provides:
                    # Do not evict asked outputs or sideffects.
                    if provide not in outputs and provide not in pruned_dag.nodes:
                        add_step_once(_EvictInstruction(provide))

            else:
                raise AssertionError("Unrecognized network graph node %r" % node)

        return steps

    def compile(
        self, inputs: Optional[Collection] = None, outputs: Optional[Collection] = None
    ) -> ExecutionPlan:
        """
        Create or get from cache an execution-plan for the given inputs/outputs.

        See :meth:`prune()` and :meth:`_build_execution_steps()`
        for detailed description.

        :param inputs:
            A collection with the names of all the given inputs.
            If `None``, all inputs that lead to given `outputs` are assumed.
        :param outputs:
            A collection or the name of the output name(s).
            If `None``, all reachable nodes from the given `inputs` are assumed.

        :return:
            the cached or fresh new execution-plan

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

            - If `outputs` asked cannot be produced by the `graph`, with msg:

                *Impossible outputs...*

            - If cannot produce any `outputs` from the given `inputs`, with msg:

                *Unsolvable graph: ...*
        """
        ## Make a stable cache-key.
        #
        if inputs is not None:
            inputs = tuple(
                sorted(astuple(inputs, "inputs", allowed_types=abc.Collection))
            )
        if outputs is not None:
            outputs = tuple(
                sorted(astuple(outputs, "outputs", allowed_types=abc.Collection))
            )
        cache_key = (inputs, outputs)

        ## Build (or retrieve from cache) execution plan
        #  for the given inputs & outputs.
        #
        if cache_key in self._cached_plans:
            plan = self._cached_plans[cache_key]
        else:
            pruned_dag, broken_edges, needs, provides = self.prune(inputs, outputs)
            steps = self._build_execution_steps(pruned_dag, needs, outputs or ())
            plan = ExecutionPlan(
                self,
                needs,
                provides,
                pruned_dag,
                tuple(broken_edges),
                tuple(steps),
                evict=outputs is not None,
            )

            self._cached_plans[cache_key] = plan

        return plan
