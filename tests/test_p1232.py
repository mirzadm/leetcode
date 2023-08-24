"""Unit tests for problem 1232"""

from src.p1232 import check_straight_line


def test_check_straight_line():
    assert check_straight_line([[1, 2], [3, 2], [4, 3]]) == False
    assert check_straight_line([[1, 2], [3, 2], [4, 2]]) == True
    assert check_straight_line([[2, 1], [3, 1], [4, 2]]) == False
    assert check_straight_line([[2, 1], [3, 1], [4, 1]]) == True
    assert check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == True
    assert (
        check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) == False
    )
