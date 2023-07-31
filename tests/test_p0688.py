"""Unit tests for problem 688"""

from src.p0688 import knight_probability


def test_knight_probability():
    assert knight_probability(1, 0, 0, 0) == 1.0
    assert knight_probability(2, 0, 0, 0) == 1.0
    assert knight_probability(2, 1, 0, 0) == 0.0
    assert knight_probability(3, 0, 0, 0) == 1.0
    assert knight_probability(3, 1, 0, 0) == 0.25
