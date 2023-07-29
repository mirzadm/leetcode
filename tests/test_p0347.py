"""Unit test for problem 347"""

from src.p0374 import guess_number


def test_guess_number():
    assert guess_number(7) == 7
    assert guess_number(10) == 7
    assert guess_number(100) == 7
