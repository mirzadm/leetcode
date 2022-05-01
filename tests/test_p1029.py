"""Unit tests for problem 1029."""
from src.p1029_two_city_scheduling import two_city_scheduling


def test_two_city_scheduling():
    assert two_city_scheduling([[1, 10], [20, 2]]) == 3
    assert two_city_scheduling([[20, 2], [1, 10]]) == 3
    assert two_city_scheduling([[1, 10], [2, 20]]) == 12
    assert two_city_scheduling([[10, 1], [20, 2]]) == 12
