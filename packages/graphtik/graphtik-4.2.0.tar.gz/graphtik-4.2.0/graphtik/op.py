# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
"""About :term:`operation` nodes (but not net-ops to break cycle)."""

import abc
import logging
from collections import abc as cabc
from collections import namedtuple
from typing import Callable, Mapping, Tuple, Union

from boltons.setutils import IndexedSet as iset

from .base import Items, Plotter, aslist, astuple, jetsam
from .modifiers import optional, sideffect, vararg, varargs

log = logging.getLogger(__name__)


def reparse_operation_data(name, needs, provides):
    """
    Validate & reparse operation data as lists.

    As a separate function to be reused by client code
    when building operations and detect errors aearly.
    """

    if not isinstance(name, cabc.Hashable):
        raise ValueError(f"Operation `name` must be hashable, got: {name}")

    # Allow single string-value for needs parameter
    needs = astuple(needs, "needs", allowed_types=cabc.Collection)
    if not all(isinstance(i, str) for i in needs):
        raise ValueError(f"All `needs` must be str, got: {needs!r}")

    # Allow single value for provides parameter
    provides = astuple(provides, "provides", allowed_types=cabc.Collection)
    if not all(isinstance(i, str) for i in provides):
        raise ValueError(f"All `provides` must be str, got: {provides!r}")

    return name, needs, provides


# TODO: immutable `Operation` by inheriting from `namedtuple`.
class Operation(abc.ABC):
    """An abstract class representing an action with :meth:`.compute()`."""

    @abc.abstractmethod
    def compute(self, named_inputs, outputs=None):
        """
        Compute (optional) asked `outputs` for the given `named_inputs`.

        It is called by :class:`.Network`.
        End-users should simply call the operation with `named_inputs` as kwargs.

        :param list named_inputs:
            the input values with which to feed the computation.
        :returns list:
            Should return a list values representing
            the results of running the feed-forward computation on
            ``inputs``.
        """


class FunctionalOperation(
    namedtuple("FnOp", "fn name needs provides parents node_props returns_dict"),
    Operation,
):
    """
    An :term:`operation` performing a callable (ie a function, a method, a
    lambda).

    .. Tip::
        Use :class:`operation()` builder class to build instances of this class instead.
    """

    def __new__(
        cls,
        fn: Callable,
        name,
        needs: Items = None,
        provides: Items = None,
        *,
        parents: Tuple = None,
        node_props: Mapping = None,
        returns_dict=None,
    ):
        """
        Build a new operation out of some function and its requirements.

        :param name:
            a name for the operation (e.g. `'conv1'`, `'sum'`, etc..);
            it will be prefixed by `parents`.
        :param needs:
            Names of input data objects this operation requires.
        :param provides:
            Names of output data objects this provides.
        :param parents:
            a tuple wth the names of the parents, prefixing `name`,
            but also kept for equality/hash check.
        :param node_props:
            added as-is into NetworkX graph
        :param returns_dict:
            if true, it means the `fn` returns a dictionary with all `provides`,
            and no further processing is done on them
            (i.e. the returned output-values are not zipped with `provides`)
        """
        node_props = node_props = node_props if node_props else {}

        if not fn or not callable(fn):
            raise ValueError(f"Operation was not provided with a callable: {fn}")
        if parents and not isinstance(parents, tuple):
            raise ValueError(f"Operation `parents` must be tuple, was {parents}")
        if node_props is not None and not isinstance(node_props, cabc.Mapping):
            raise ValueError(f"Operation `node_props` must be a dict, was {node_props}")

        ## Overwrite reparsed op-data.
        name = ".".join(str(pop) for pop in ((parents or ()) + (name,)))
        name, needs, provides = reparse_operation_data(name, needs, provides)
        return super().__new__(
            cls, fn, name, needs, provides, parents, node_props, returns_dict
        )

    def __eq__(self, other):
        """Operation identity is based on `name` and `parents`."""
        return bool(
            self.name is not None
            and self.name == getattr(other, "name", None)
            and self.parents == getattr(other, "parents", None)
        )

    def __hash__(self):
        """Operation identity is based on `name` and `parents`."""
        return hash(self.name) ^ hash(self.parents)

    def __repr__(self):
        """
        Display more informative names for the Operation class
        """
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        fn_name = self.fn and getattr(self.fn, "__name__", str(self.fn))
        returns_dict_marker = self.returns_dict and "{}" or ""
        nprops = f", x{len(self.node_props)}props" if self.node_props else ""
        return (
            f"FunctionalOperation(name={self.name!r}, needs={needs!r}, "
            f"provides={provides!r}, fn{returns_dict_marker}={fn_name!r}{nprops})"
        )

    def withset(self, **kw) -> "FunctionalOperation":
        """
        Make a clone with the some values replaced.

        .. ATTENTION::
            Using :meth:`namedtuple._replace()` would not pass through cstor,
            so would not get a nested `name` with `parents`, not arguments validation.
        """
        fn = kw["fn"] if "fn" in kw else self.fn
        name = kw["name"] if "name" in kw else self.name
        needs = kw["needs"] if "needs" in kw else self.needs
        provides = kw["provides"] if "provides" in kw else self.provides

        return FunctionalOperation(fn, name, needs, provides, **kw)

    def _zip_results_with_provides(self, results, real_provides: iset) -> dict:
        """Zip results with expected "real" (without sideffects) `provides`."""
        if not real_provides:  # All outputs were sideffects?
            if results:
                ## Do not scream,
                #  it is common to call a function for its sideffects,
                # which happens to return an irrelevant value.
                log.warning(
                    "Ignoring result(%s) because no `provides` given!\n  %s",
                    results,
                    self,
                )
            results = {}
        elif not self.returns_dict:
            nexpected = len(real_provides)

            if nexpected > 1 and (
                not isinstance(results, cabc.Iterable) or len(results) != nexpected
            ):
                raise ValueError(
                    f"Expected x{nexpected} ITERABLE results, got: {results}"
                )

            if nexpected == 1:
                results = [results]

            results = dict(zip(real_provides, results))

        if self.returns_dict:
            if not isinstance(results, cabc.Mapping):
                raise ValueError(f"Expected dict-results, got: {results}\n  {self}")
        if set(results) != real_provides:
            raise ValueError(
                f"Results({results}) mismatched provides({real_provides})!\n  {self}"
            )

        return results

    def compute(self, named_inputs, outputs=None) -> dict:
        try:
            try:
                args = [
                    ## Network expected to ensure all compulsory inputs exist,
                    #  so no special handling for key errors here.
                    #
                    named_inputs[
                        n
                    ]  # Key-error here means `inputs` < compulsory `needs`.
                    for n in self.needs
                    if not isinstance(n, (optional, sideffect))
                ]
            except KeyError:
                compulsory = iset(
                    n for n in self.needs if not isinstance(n, (optional, sideffect))
                )
                raise ValueError(
                    f"Missing compulsory needs{list(compulsory)}!\n  inputs: {list(named_inputs)}\n  {self}"
                )

            args.extend(
                named_inputs[n]
                for n in self.needs
                if isinstance(n, vararg) and n in named_inputs
            )
            args.extend(
                nn
                for n in self.needs
                if isinstance(n, varargs) and n in named_inputs
                for nn in named_inputs[n]
            )

            # Find any optional inputs in named_inputs.  Get only the ones that
            # are present there, no extra `None`s.
            optionals = {
                n: named_inputs[n]
                for n in self.needs
                if isinstance(n, optional)
                and not isinstance(n, (vararg, varargs))
                and n in named_inputs
            }

            results_fn = self.fn(*args, **optionals)

            provides = iset(n for n in self.provides if not isinstance(n, sideffect))
            results_op = self._zip_results_with_provides(results_fn, provides)

            if outputs:
                outputs = set(n for n in outputs if not isinstance(n, sideffect))
                # Ignore sideffect outputs.
                results_op = {
                    key: val for key, val in results_op.items() if key in outputs
                }

            return results_op
        except Exception as ex:
            jetsam(
                ex,
                locals(),
                "outputs",
                "provides",
                "results_fn",
                "results_op",
                operation="self",
                args=lambda locs: {
                    "args": locs.get("args"),
                    "kwargs": locs.get("optionals"),
                },
            )

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


class operation:
    """
    A builder for graph-operations wrapping functions.

    :param function fn:
        The function used by this operation.  This does not need to be
        specified when the operation object is instantiated and can instead
        be set via ``__call__`` later.
    :param str name:
        The name of the operation in the computation graph.
    :param list needs:
        Names of input data objects this operation requires.  These should
        correspond to the ``args`` of ``fn``.
    :param list provides:
        Names of output data objects this operation provides.
        If more than one given, those must be returned in an iterable,
        unless `returns_dict` is true, in which cae a dictionary with as many
        elements must be returned
    :param bool returns_dict:
        if true, it means the `fn` returns a dictionary with all `provides`,
        and no further processing is done on them
        (i.e. the returned output-values are not zipped with `provides`)
    :param node_props:
        added as-is into NetworkX graph

    :return:
        when called, it returns a :class:`FunctionalOperation`

    **Example:**

    This is an example of its use, based on the "builder pattern"::

        >>> from graphtik import operation

        >>> opb = operation(name='add_op')
        >>> opb.withset(needs=['a', 'b'])
        operation(name='add_op', needs=['a', 'b'], provides=[], fn=None)
        >>> opb.withset(provides='SUM', fn=sum)
        operation(name='add_op', needs=['a', 'b'], provides=['SUM'], fn='sum')

    You may keep calling ``withset()`` till you invoke a final ``__call__()``
    on the builder;  then you get the actual :class:`.FunctionalOperation` instance::

        >>> # Create `Operation` and overwrite function at the last moment.
        >>> opb(sum)
        FunctionalOperation(name='add_op', needs=['a', 'b'], provides=['SUM'], fn='sum')

    .. Tip::
        Remember to call once more the builder class at the end, to get the actual
        operation instance.

    """

    def __init__(
        self,
        fn: Callable = None,
        *,
        name=None,
        needs: Items = None,
        provides: Items = None,
        returns_dict=None,
        node_props: Mapping = None,
    ):
        self.fn = fn
        self.name = name
        self.needs = needs
        self.provides = provides
        self.returns_dict = returns_dict
        self.node_props = node_props

    def withset(
        self,
        *,
        fn: Callable = None,
        name=None,
        needs: Items = None,
        provides: Items = None,
        returns_dict=None,
        node_props: Mapping = None,
    ) -> "operation":
        if fn is not None:
            self.fn = fn
        if name is not None:
            self.name = name
        if needs is not None:
            self.needs = needs
        if provides is not None:
            self.provides = provides
        if returns_dict is not None:
            self.returns_dict = returns_dict
        if node_props is not None:
            self.node_props = node_props

        return self

    def __call__(
        self,
        fn: Callable = None,
        *,
        name=None,
        needs: Items = None,
        provides: Items = None,
        returns_dict=None,
        node_props: Mapping = None,
    ) -> FunctionalOperation:
        """
        This enables ``operation`` to act as a decorator or as a functional
        operation, for example::

            @operator(name='myadd1', needs=['a', 'b'], provides=['c'])
            def myadd(a, b):
                return a + b

        or::

            def myadd(a, b):
                return a + b
            operator(name='myadd1', needs=['a', 'b'], provides=['c'])(myadd)

        :param function fn:
            The function to be used by this ``operation``.

        :return:
            Returns an operation class that can be called as a function or
            composed into a computation graph.
        """

        self.withset(
            fn=fn,
            name=name,
            needs=needs,
            provides=provides,
            returns_dict=returns_dict,
            node_props=node_props,
        )

        return FunctionalOperation(**vars(self))

    def __repr__(self):
        """
        Display more informative names for the Operation class
        """
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        fn_name = self.fn and getattr(self.fn, "__name__", str(self.fn))
        nprops = f", x{len(self.node_props)}props" if self.node_props else ""
        return (
            f"operation(name={self.name!r}, needs={needs!r}, "
            f"provides={provides!r}, fn={fn_name!r}{nprops})"
        )
