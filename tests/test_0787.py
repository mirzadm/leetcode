"""Unit tests for problem 787"""

from src.p0787 import find_cheapest_price


def test_find_cheapest_price():
    assert find_cheapest_price(n=2, flights=[[0, 1, 100]], src=0, dst=1, k=0) == 100
    assert find_cheapest_price(n=2, flights=[[0, 1, 100]], src=0, dst=1, k=1) == 100
    assert (
        find_cheapest_price(
            n=2, flights=[[0, 1, 100], [0, 2, 500], [1, 2, 200]], src=0, dst=2, k=0
        )
        == 500
    )
    assert (
        find_cheapest_price(
            n=3, flights=[[0, 1, 100], [0, 2, 500], [1, 2, 200]], src=0, dst=2, k=1
        )
        == 300
    )
    assert (
        find_cheapest_price(
            n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1
        )
        == 6
    )
    assert (
        find_cheapest_price(
            n=4,
            flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            src=0,
            dst=3,
            k=1,
        )
        == 700
    )
