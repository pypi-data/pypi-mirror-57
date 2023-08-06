# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
"""About network-operations (those based on graphs)"""

import logging
import re
from collections import abc
from typing import Any, Callable, Mapping

import networkx as nx
from boltons.setutils import IndexedSet as iset

from .base import Items, Plotter, aslist, astuple, jetsam
from .modifiers import optional, sideffect
from .network import Network, yield_operations
from .op import FunctionalOperation, Operation, reparse_operation_data

log = logging.getLogger(__name__)


class NetworkOperation(Operation, Plotter):
    """
    An Operation performing a network-graph of other operations.

    .. Tip::
        Use :func:`compose()` factory to prepare the `net` and build
        instances of this class.
    """

    #: set execution mode to single-threaded sequential by default
    method = None
    overwrites_collector = None
    #: The execution_plan of the last call to compute(), stored as debugging aid.
    last_plan = None
    #: The inputs names (possibly `None`) used to compile the :attr:`plan`.
    inputs = None
    #: The outputs names (possibly `None`) used to compile the :attr:`plan`.
    outputs = None

    def __init__(
        self,
        net,
        name,
        *,
        inputs=None,
        outputs=None,
        predicate: Callable[[Any, Mapping], bool] = None,
        method=None,
        overwrites_collector=None,
    ):
        """
        :param inputs:
            see :meth:`narrowed()`
        :param outputs:
            see :meth:`narrowed()`
        :param predicate:
            a 2-argument callable(op, node-data) that should return true for nodes to include
        :param method:
            either `parallel` or None (default);
            if ``"parallel"``, launches multi-threading.
            Set when invoking a composed graph or by
            :meth:`~NetworkOperation.set_execution_method()`.
        :param overwrites_collector:
            (optional) a mutable dict to be fillwed with named values.
            If missing, values are simply discarded.

        :raises ValueError:
            see :meth:`narrowed()`
        """
        ## Set data asap, for debugging, although `net.narrowed()` will reset them.
        self.name = name
        self.inputs = inputs
        self.provides = outputs
        self.set_execution_method(method)
        self.set_overwrites_collector(overwrites_collector)

        # TODO: Is it really necessary to sroe IO on netop?
        self.inputs = inputs
        self.outputs = outputs

        # Prune network
        self.net = net.narrowed(inputs, outputs, predicate)
        self.name, self.needs, self.provides = reparse_operation_data(
            self.name, self.net.needs, self.net.provides
        )

    def __repr__(self):
        """
        Display more informative names for the Operation class
        """
        clsname = type(self).__name__
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        nops = sum(1 for i in yield_operations(self.net.graph))
        return (
            f"{clsname}({self.name!r}, needs={needs}, provides={provides}, x{nops}ops)"
        )

    def narrowed(
        self,
        inputs: Items = None,
        outputs: Items = None,
        name=None,
        predicate: Callable[[Any, Mapping], bool] = None,
    ) -> "NetworkOperation":
        """
        Return a copy with a network pruned for the given `needs` & `provides`.

        :param inputs:
            prune `net` against these possbile inputs for :meth:`compute()`;
            method will WARN for any irrelevant inputs given.
            If `None`, they are collected from the :attr:`net`.
            They become the `needs` of the returned `netop`.
        :param outputs:
            prune `net` against these possible outputs for :meth:`compute()`;
            method will RAISE if any irrelevant outputs asked.
            If `None`, they are collected from the :attr:`net`.
            They become the `provides` of the returned `netop`.
        :param name:
            the name for the new netop:

            - if `None`, the same name is kept;
            - if True, a distinct name is  devised::

                <old-name>-<uid>

            - otherwise, the given `name` is applied.
        :param predicate:
            a 2-argument callable(op, node-data) that should return true for nodes to include

        :return:
            A narrowed netop clone, which **MIGHT be empty!***

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

        """
        if name is None:
            name = self.name
        elif name is True:
            name = self.name

            ## Devise a new UID based on inputs & outputs.
            #
            uid = str(abs(hash(f"{inputs}{outputs}")))[:7]
            m = re.match(r"^(.*)-(\d+)$", name)
            if m:
                name = m.group(1)
            name = f"{name}-{uid}"

        return NetworkOperation(
            self.net,
            name,
            inputs=inputs,
            outputs=outputs,
            predicate=predicate,
            method=self.method,
            overwrites_collector=self.overwrites_collector,
        )

    def _build_pydot(self, **kws):
        """delegate to network"""
        kws.setdefault("title", self.name)
        plotter = self.last_plan or self.net
        return plotter._build_pydot(**kws)

    def compute(self, named_inputs, outputs=None) -> dict:
        """
        Solve & execute the graph, sequentially or parallel.

        It see also :meth:`.Operation.compute()`.

        :param dict named_inputs:
            A maping of names --> values that must contain at least
            the compulsory inputs that were specified when the plan was built
            (but cannot enforce that!).
            Cloned, not modified.
        :param outputs:
            a string or a list of strings with all data asked to compute.
            If you set this variable to ``None``, all data nodes will be kept
            and returned at runtime.

        :returns:
            a dictionary of output data objects, keyed by name.

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

            - If plan does not contain any operations, with msg:

                *Unsolvable graph: ...*

            - If given `inputs` mismatched plan's :attr:`needs`, with msg:

                *Plan needs more inputs...*

            - If `outputs` asked cannot be produced by the :attr:`dag`, with msg:

                *Impossible outputs...*
        """
        try:
            net = self.net

            # Build the execution plan.
            self.last_plan = plan = net.compile(named_inputs.keys(), outputs)

            solution = plan.execute(
                named_inputs,
                outputs,
                overwrites=self.overwrites_collector,
                method=self.execution_method,
            )

            return solution
        except Exception as ex:
            jetsam(ex, locals(), "plan", "solution", "outputs", network="net")

    def __call__(self, **input_kwargs) -> dict:
        """
        Delegates to :meth:`compute()`, respecting any narrowed `outputs`.
        """
        # To respect narrowed `outputs` must send them due to recompilation.
        return self.compute(input_kwargs, outputs=self.outputs)

    def set_execution_method(self, method):
        """
        Determine how the network will be executed.

        :param str method:
            If "parallel", execute graph operations concurrently
            using a threadpool.
        """
        choices = ["parallel", None]
        if method not in choices:
            raise ValueError(
                "Invalid computation method %r!  Must be one of %s" % (method, choices)
            )
        self.execution_method = method

    def set_overwrites_collector(self, collector):
        """
        Asks to put all *overwrites* into the `collector` after computing

        An "overwrites" is intermediate value calculated but NOT stored
        into the results, becaues it has been given also as an intemediate
        input value, and the operation that would overwrite it MUST run for
        its other results.

        :param collector:
            a mutable dict to be fillwed with named values
        """
        if collector is not None and not isinstance(collector, abc.MutableMapping):
            raise ValueError(
                "Overwrites collector was not a MutableMapping, but: %r" % collector
            )
        self.overwrites_collector = collector


def compose(
    name,
    op1,
    *operations,
    needs: Items = None,
    provides: Items = None,
    merge=False,
    node_props=None,
    method=None,
    overwrites_collector=None,
) -> NetworkOperation:
    """
    Composes a collection of operations into a single computation graph,
    obeying the ``merge`` property, if set in the constructor.

    :param str name:
        A optional name for the graph being composed by this object.
    :param op1:
        syntactically force at least 1 operation
    :param operations:
        Each argument should be an operation instance created using
        ``operation``.
    :param bool merge:
        If ``True``, this compose object will attempt to merge together
        ``operation`` instances that represent entire computation graphs.
        Specifically, if one of the ``operation`` instances passed to this
        ``compose`` object is itself a graph operation created by an
        earlier use of ``compose`` the sub-operations in that graph are
        compared against other operations passed to this ``compose``
        instance (as well as the sub-operations of other graphs passed to
        this ``compose`` instance).  If any two operations are the same
        (based on name), then that operation is computed only once, instead
        of multiple times (one for each time the operation appears).
    :param node_props:
        added as-is into NetworkX graph, to provide for filtering
        by :meth:`.NetworkOperation.narrowed()`.
    :param method:
        either `parallel` or None (default);
        if ``"parallel"``, launches multi-threading.
        Set when invoking a composed graph or by
        :meth:`~NetworkOperation.set_execution_method()`.
    :param overwrites_collector:
        (optional) a mutable dict to be fillwed with named values.
        If missing, values are simply discarded.

    :return:
        Returns a special type of operation class, which represents an
        entire computation graph as a single operation.

    :raises ValueError:
        If the `net`` cannot produce the asked `outputs` from the given `inputs`.
    """
    operations = (op1,) + operations
    if not all(isinstance(op, Operation) for op in operations):
        raise ValueError(f"Non-Operation instances given: {operations}")

    def proc_op(op, parent=None):
        """clone FuncOperation with certain props changed"""
        assert isinstance(op, FunctionalOperation), op

        ## Convey any node-props specified in the netop here
        #  to all sub-operations.
        #
        if node_props or (not merge and parent):
            kw = {}
            if node_props:
                op_node_props = op.node_props.copy()
                op_node_props.update(node_props)
                kw["node_props"] = op_node_props
            ## If `merge` asked, leave original `name` to deduplicate operations,
            #  otherwise rename the op by prefixing them with their parent netop.
            #
            if not merge and parent:
                kw["parents"] = (parent,) + (op.parents or ())
            op = op.withset(**kw)

        return op

    merge_set = iset()  # Preseve given node order.
    for op in operations:
        if isinstance(op, NetworkOperation):
            merge_set.update(
                proc_op(s, op.name) for s in op.net.graph if isinstance(s, Operation)
            )
        else:
            merge_set.add(proc_op(op))
    operations = merge_set

    net = Network(*operations)

    return NetworkOperation(
        net,
        name,
        inputs=needs,
        outputs=provides,
        method=method,
        overwrites_collector=overwrites_collector,
    )
