import unittest
from src.p0015_sum_of_three import (
    sum_of_three_n2_partition as sum_n2_partition,
)


class TestCases(unittest.TestCase):
    def test_sum_n2_partition(self):
        self.assertEqual(sum_n2_partition([]), [])
        self.assertEqual(sum_n2_partition([1]), [])
        self.assertEqual(sum_n2_partition([1, 2]), [])
        self.assertEqual(sum_n2_partition([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(sum_n2_partition([0, 0, 1]), [])
        self.assertEqual(sum_n2_partition([-1, 0, 1]), [[-1, 0, 1]])
        self.assertEqual(sum_n2_partition([-1, 1, 2]), [])
        self.assertEqual(sum_n2_partition([-1, -1, 2]), [[-1, -1, 2]])
        self.assertEqual(sum_n2_partition(
            [-1, -1, 2, -1, -1, 2]), [[-1, -1, 2]]
        )
        result = sum_n2_partition([-1, -1, 2, 1, 0, -1])
        self.assertEqual(sorted(result), [[-1, -1, 2], [-1, 0, 1]])
