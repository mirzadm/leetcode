import unittest
from src.p0015_sum_of_three import (
    sum_of_three_brute_force as sum_n3,
    sum_of_three_n2 as sum_n2,
)


class TestCases(unittest.TestCase):
    def test_sum_n3(self):
        self.assertEqual(sum_n3([]), [])
        self.assertEqual(sum_n3([1]), [])
        self.assertEqual(sum_n3([1, 2]), [])
        self.assertEqual(sum_n3([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(sum_n3([-1, -1, 2]), [[-1, -1, 2]])
        self.assertEqual(sum_n3([-1, -1, 2, 1, 0, -1]), [[-1, -1, 2], [-1, 0, 1]])

    def test_sum_n2(self):
        self.assertEqual(sum_n2([]), [])
        self.assertEqual(sum_n2([1]), [])
        self.assertEqual(sum_n2([1, 2]), [])
        self.assertEqual(sum_n2([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(sum_n2([-1, -1, 2]), [[-1, -1, 2]])
        self.assertEqual(sum_n2([-1, -1, 2, 1, 0, -1]), [[-1, -1, 2], [-1, 0, 1]])
