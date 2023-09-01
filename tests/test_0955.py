"""Unit tests for problem 955."""

from src.p0955 import min_deletion_size


def test_min_deletion_size():
    assert min_deletion_size(['a']) == 0
    assert min_deletion_size(['a', 'a']) == 0
    assert min_deletion_size(['a', 'b']) == 0
    assert min_deletion_size(['b', 'a']) == 1
    assert min_deletion_size(['ba', 'ab']) == 1
    assert min_deletion_size(['bb', 'ba']) == 1
