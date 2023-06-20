from src.p0910_smallest_range_2_sliding_window import smallest_range_2_sliding_window
from src.p0910_smallest_range_2_partition import smallest_range_2_partition


def test_smallest_range_2_sliding_window():
    assert smallest_range_2_sliding_window([1], 0) == 0
    assert smallest_range_2_sliding_window([1], 1) == 0
    assert smallest_range_2_sliding_window([1], 5) == 0

    assert smallest_range_2_sliding_window([1, 2], 0) == 1
    assert smallest_range_2_sliding_window([1, 2], 1) == 1
    assert smallest_range_2_sliding_window([1, 2], 5) == 1

    assert smallest_range_2_sliding_window([2, 1], 0) == 1
    assert smallest_range_2_sliding_window([2, 1], 1) == 1
    assert smallest_range_2_sliding_window([2, 1], 5) == 1

    assert smallest_range_2_sliding_window([1, 3, 6], 0) == 5
    assert smallest_range_2_sliding_window([1, 3, 6], 1) == 3
    assert smallest_range_2_sliding_window([1, 3, 6], 3) == 3
    assert smallest_range_2_sliding_window([1, 3, 6], 10) == 5


def test_smallest_range_2_partition():
    assert smallest_range_2_partition([1], 0) == 0
    assert smallest_range_2_partition([1], 1) == 0
    assert smallest_range_2_partition([1], 5) == 0

    assert smallest_range_2_partition([1, 2], 0) == 1
    assert smallest_range_2_partition([1, 2], 1) == 1
    assert smallest_range_2_partition([1, 2], 5) == 1

    assert smallest_range_2_partition([2, 1], 0) == 1
    assert smallest_range_2_partition([2, 1], 1) == 1
    assert smallest_range_2_partition([2, 1], 5) == 1

    assert smallest_range_2_partition([1, 3, 6], 0) == 5
    assert smallest_range_2_partition([1, 3, 6], 1) == 3
    assert smallest_range_2_partition([1, 3, 6], 3) == 3
    assert smallest_range_2_partition([1, 3, 6], 10) == 5
