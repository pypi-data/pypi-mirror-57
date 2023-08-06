# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
import functools as fnt
import itertools as itt
import logging

import pytest

from graphtik import base, network, op, operation
from graphtik.netop import NetworkOperation
from graphtik.network import Solution


@pytest.mark.parametrize("locs", [None, (), [], [0], "bad"])
def test_jetsam_bad_locals(locs, caplog):
    caplog.set_level(logging.INFO)
    with pytest.raises(AssertionError, match="Bad `locs`") as excinfo:
        try:
            raise Exception()
        except Exception as ex:
            base.jetsam(ex, locs, a="a")

    assert not hasattr(excinfo.value, "jetsam")
    assert "Supressed error while annotating exception" not in caplog.text


@pytest.mark.parametrize("keys", [{"k": None}, {"k": ()}, {"k": []}, {"k": [0]}])
def test_jetsam_bad_keys(keys, caplog):
    caplog.set_level(logging.INFO)
    with pytest.raises(AssertionError, match="Bad `salvage_mappings`") as excinfo:
        try:
            raise Exception("ABC")
        except Exception as ex:
            base.jetsam(ex, {}, **keys)

    assert not hasattr(excinfo.value, "jetsam")
    assert "Supressed error while annotating exception" not in caplog.text


@pytest.mark.parametrize("locs", [None, (), [], [0], "bad"])
def test_jetsam_bad_locals_given(locs, caplog):
    caplog.set_level(logging.INFO)
    with pytest.raises(AssertionError, match="Bad `locs`") as excinfo:
        try:
            raise Exception("ABC")
        except Exception as ex:
            base.jetsam(ex, locs, a="a")

    assert not hasattr(excinfo.value, "jetsam")
    assert "Supressed error while annotating exception" not in caplog.text


@pytest.mark.parametrize("annotation", [None, (), [], [0], "bad"])
def test_jetsam_bad_existing_annotation(annotation, caplog):
    caplog.set_level(logging.INFO)
    with pytest.raises(Exception, match="ABC") as excinfo:
        try:
            ex = Exception("ABC")
            ex.jetsam = annotation
            raise ex
        except Exception as ex:
            base.jetsam(ex, {}, a="a")

    assert excinfo.value.jetsam == {"a": None}
    assert "Supressed error while annotating exception" not in caplog.text


def test_jetsam_dummy_locals(caplog):
    with pytest.raises(Exception, match="ABC") as excinfo:
        try:
            raise Exception("ABC")
        except Exception as ex:
            base.jetsam(ex, {"a": 1}, a="a", bad="bad")

    assert isinstance(excinfo.value.jetsam, dict)
    assert excinfo.value.jetsam == {"a": 1, "bad": None}
    assert "Supressed error" not in caplog.text


def _scream(*args, **kwargs):
    raise Exception("ABC")


def _jetsamed_fn(*args, **kwargs):
    b = 1
    try:
        a = 1
        b = 2
        _scream()
    except Exception as ex:
        base.jetsam(ex, locals(), a="a", b="b")


def test_jetsam_locals_simple(caplog):
    with pytest.raises(Exception, match="ABC") as excinfo:
        _jetsamed_fn()
    assert excinfo.value.jetsam == {"a": 1, "b": 2}
    assert "Supressed error" not in caplog.text


def test_jetsam_nested():
    def inner():
        try:
            a = 0
            fn = "inner"
            _jetsamed_fn()
        except Exception as ex:
            base.jetsam(ex, locals(), fn="fn")

    def outer():
        try:

            fn = "outer"
            b = 0
            inner()
        except Exception as ex:
            base.jetsam(ex, locals(), fn="fn")

    with pytest.raises(Exception, match="ABC") as excinfo:
        outer()

    assert excinfo.value.jetsam == {"fn": "inner", "a": 1, "b": 2}


class _ScreamingOperation(op.Operation):
    def __init__(self):
        self.name = ("",)
        self.needs = ()
        self.provides = ("a",)
        self.node_props = {}

    def compute(self, named_inputs, outputs=None):
        _scream()


@pytest.mark.parametrize(
    "acallable, expected_jetsam",
    [
        # NO old-stuff Operation(fn=_jetsamed_fn, name="test", needs="['a']", provides=[]),
        (
            fnt.partial(
                operation(name="test", needs=["a"], provides=["b"])(_scream).compute,
                named_inputs={"a": 1},
            ),
            "outputs provides aliases results_fn results_op operation args".split(),
        ),
        (
            fnt.partial(
                network.ExecutionPlan(*([None] * 6))._call_operation,
                op=_ScreamingOperation(),
                solution=Solution(None),
                endurance=None,
            ),
            ["plan", "solution"],
        ),
        # Not easy to test Network calling a screaming func (see next TC).
    ],
)
def test_jetsam_sites_screaming_func(acallable, expected_jetsam):
    # Check jetsams when the underlying function fails.
    with pytest.raises(Exception, match="ABC") as excinfo:
        acallable()

    ex = excinfo.value
    assert hasattr(ex, "jetsam"), acallable
    assert set(ex.jetsam.keys()) == set(expected_jetsam)


class _DummyOperation(op.Operation):
    def __init__(self):
        self.name = ("",)
        self.needs = ()
        self.provides = ("a",)
        self.node_props = {}

    def compute(self, named_inputs, outputs=None):
        pass


@pytest.mark.parametrize(
    "acallable, expected_jetsam",
    [
        # NO old-stuff Operation(fn=_jetsamed_fn, name="test", needs="['a']", provides=[]),
        (
            fnt.partial(operation(_scream, name="test")().compute, named_inputs=None),
            "outputs provides aliases results_fn results_op operation args".split(),
        ),
        (
            fnt.partial(
                network.ExecutionPlan(*([None] * 6))._call_operation,
                op=operation(_scream, name="auch")(),
                solution=Solution(None),
                endurance=None,
            ),
            "solution outputs provides aliases results_fn results_op operation args plan".split(),
        ),
        (
            fnt.partial(
                network.ExecutionPlan(*([None] * 6)).execute, named_inputs=None
            ),
            ["solution"],
        ),
        (
            fnt.partial(
                NetworkOperation(network.Network(_DummyOperation()), None).compute,
                named_inputs=None,
                outputs="bad",
            ),
            "network plan solution outputs".split(),
        ),
    ],
)
def test_jetsam_sites_scream(acallable, expected_jetsam):
    # Check jetsams when the site fails.
    with pytest.raises(Exception) as excinfo:
        acallable()

    ex = excinfo.value
    assert hasattr(ex, "jetsam"), acallable
    assert set(ex.jetsam.keys()) == set(expected_jetsam)
