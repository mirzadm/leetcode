"""Unit tests for problem 1913."""

from src.p1913_max_product_diff import max_product_difference


def test_max_product_difference():
    assert max_product_difference([1, 1, 1, 1]) == 0
    assert max_product_difference([1, 1, 2, 2]) == 3
    assert max_product_difference([1, 1, 1, 2]) == 1
    assert max_product_difference([1, 2, 2, 4]) == 6
