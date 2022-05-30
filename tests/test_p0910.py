from src.p0910_smallest_range_2 import smallest_range_2


def test_smallest_range_2():
    assert smallest_range_2([1], 0) == 0
    assert smallest_range_2([1], 1) == 0
    assert smallest_range_2([1], 5) == 0

    assert smallest_range_2([1, 2], 0) == 1
    assert smallest_range_2([1, 2], 1) == 1
    assert smallest_range_2([1, 2], 5) == 1

    assert smallest_range_2([2, 1], 0) == 1
    assert smallest_range_2([2, 1], 1) == 1
    assert smallest_range_2([2, 1], 5) == 1

    assert smallest_range_2([1, 3, 6], 0) == 5
    assert smallest_range_2([1, 3, 6], 1) == 3
    assert smallest_range_2([1, 3, 6], 3) == 3
    assert smallest_range_2([1, 3, 6], 10) == 5
