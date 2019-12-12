import unittest
from src.p0015_sum_of_three import (
    sum_of_three_brute_force as brute_force,
)


class TestCases(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(brute_force([]), [])
        self.assertEqual(brute_force([1]), [])
        self.assertEqual(brute_force([1, 2]), [])
        self.assertEqual(brute_force([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(brute_force([-1, -1, 2]), [[-1, -1, 2]])
        self.assertEqual(brute_force([-1, -1, 2, 1, 0, -1]), [[-1, -1, 2], [-1, 0, 1]])
