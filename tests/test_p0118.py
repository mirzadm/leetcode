"""Unit tests for problem 118"""

from src.p0118_khayyam_triangle import khayyam_triangle


def test_khayyam_triangle():
    assert khayyam_triangle(1) == [[1]]
    assert khayyam_triangle(2) == [[1], [1, 1]]
    assert khayyam_triangle(3) == [[1], [1, 1], [1, 2, 1]]
    assert khayyam_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
