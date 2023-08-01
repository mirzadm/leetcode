"""Unit tests for problem 665"""

from src.p0665 import is_convertible_to_non_decreasing_array as check_array


def test_check_array():
    assert check_array([1]) == True
    assert check_array([1, 1]) == True
    assert check_array([1, 2]) == True
    assert check_array([2, 1]) == True
    assert check_array([1, 1, 2]) == True
    assert check_array([2, 1, 0]) == False
    assert check_array([2, 1, 1]) == True
    assert check_array([1, 2, 1]) == True
    assert check_array([1, 2, 1, 3]) == True
