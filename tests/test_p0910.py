import unittest
from src.p0910_smallest_range_2 import smallest_range_2


class TestCases(unittest.TestCase):
    def test_smallest_range_2(self):
        self.assertEqual(smallest_range_2([1], 0), 0)
        self.assertEqual(smallest_range_2([1], 1), 0)
        self.assertEqual(smallest_range_2([1], 5), 0)

        self.assertEqual(smallest_range_2([1, 2], 0), 1)
        self.assertEqual(smallest_range_2([1, 2], 1), 1)
        self.assertEqual(smallest_range_2([1, 2], 5), 1)

        self.assertEqual(smallest_range_2([2, 1], 0), 1)
        self.assertEqual(smallest_range_2([2, 1], 1), 1)
        self.assertEqual(smallest_range_2([2, 1], 5), 1)

        self.assertEqual(smallest_range_2([1, 3, 6], 0), 5)
        self.assertEqual(smallest_range_2([1, 3, 6], 1), 3)
        self.assertEqual(smallest_range_2([1, 3, 6], 3), 3)
