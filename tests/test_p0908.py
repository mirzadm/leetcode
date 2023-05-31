from src.p0908_smallest_range_1 import smallest_range


def test_smallest_range():
    assert smallest_range([1], 0) == 0
    assert smallest_range([1], 1) == 0
    assert smallest_range([1], 5) == 0

    assert smallest_range([1, 2], 0) == 1
    assert smallest_range([1, 2], 1) == 0
    assert smallest_range([1, 2], 5) == 0

    assert smallest_range([2, 1], 0) == 1
    assert smallest_range([2, 1], 1) == 0
    assert smallest_range([2, 1], 5) == 0

    assert smallest_range([1, 3, 6], 0) == 5
    assert smallest_range([1, 3, 6], 1) == 3
    assert smallest_range([1, 3, 6], 2) == 1
    assert smallest_range([1, 3, 6], 3) == 0
    assert smallest_range([1, 3, 6], 10) == 0
