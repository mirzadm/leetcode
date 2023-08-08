"""Unit tests for problem 2640"""

from src.p2640 import find_prefix_score


def test_find_prefix_score():
    assert find_prefix_score([1]) == [2]
    assert find_prefix_score([1, 2]) == [2, 6]
    assert find_prefix_score([2, 1]) == [4, 7]
    assert find_prefix_score([2, 1, 3]) == [4, 7, 13]
