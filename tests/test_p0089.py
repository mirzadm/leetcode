"""Unit tests for problem 89."""

import pytest
from src.p0089_gray_code import (
    _convert_to_int,
    _powers_of_two,
    gray_code_sequence_generator as gray_code,
)

def test_convert_to_int():
    with pytest.raises(ValueError):
        _convert_to_int([])
    assert _convert_to_int([0]) == 0
    assert _convert_to_int([0, 0]) == 0
    assert _convert_to_int([1]) == 1
    assert _convert_to_int([1, 0]) == 1
    assert _convert_to_int([0, 1]) == 2
    assert _convert_to_int([1, 1]) == 3
    assert _convert_to_int([0, 0, 1]) == 4

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
