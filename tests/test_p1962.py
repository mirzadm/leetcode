"""Unit tests for problem 1962"""

from src.p1962 import min_stone_sum


def test_min_stone_sum():
    assert min_stone_sum([1], 1) == 1
    assert min_stone_sum([1], 2) == 1
    assert min_stone_sum([1], 10) == 1
    assert min_stone_sum([2], 1) == 1
    assert min_stone_sum([2], 2) == 1
    assert min_stone_sum([2], 10) == 1
    assert min_stone_sum([3], 1) == 2
    assert min_stone_sum([3], 2) == 1
    assert min_stone_sum([3], 10) == 1
    assert min_stone_sum([1, 1], 1) == 2
    assert min_stone_sum([1, 1], 2) == 2
    assert min_stone_sum([1, 1], 10) == 2
    assert min_stone_sum([1, 2], 1) == 2
    assert min_stone_sum([1, 2], 2) == 2
    assert min_stone_sum([1, 2], 10) == 2
    assert min_stone_sum([1, 3, 31], 1) == 20
    assert min_stone_sum([1, 3, 31], 2) == 12
    assert min_stone_sum([1, 3, 31], 3) == 8
    assert min_stone_sum([1, 3, 31], 4) == 6
    assert min_stone_sum([1, 3, 31], 5) == 5
    assert min_stone_sum([1, 3, 31], 6) == 4
    assert min_stone_sum([1, 3, 31], 7) == 3
    assert min_stone_sum([1, 3, 31], 8) == 3
