"""Unit tests for problem 89."""

import pytest
from src.p0089_gray_code import (
    _powers_of_two,
    gray_code_sequence_generator as gray_code,
    gray_code_formula,
)


def test_powers_of_two():
    with pytest.raises(ValueError):
        _powers_of_two(-1)
    assert _powers_of_two(0) == [1]
    assert _powers_of_two(1) == [1, 2]
    assert _powers_of_two(2) == [1, 2, 4]
    assert _powers_of_two(3) == [1, 2, 4, 8]

def test_gray_code():
    with pytest.raises(ValueError):
        gray_code(0)
    assert gray_code(1) == [0, 1]
    assert gray_code(2) == [0, 1, 3, 2]
    assert gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]

def test_gray_code_formula():
    with pytest.raises(ValueError):
        gray_code_formula(0)
    assert gray_code(1) == [0, 1]
    assert gray_code(2) == [0, 1, 3, 2]
    assert gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]
