import unittest
from src.p1029_two_city_scheduling import two_city_scheduling


class TestCases(unittest.TestCase):
    def test_two_city_scheduling(self):
        self.assertEqual(two_city_scheduling([[1, 10], [20, 2]]), 3)
        self.assertEqual(two_city_scheduling([[20, 2], [1, 10]]), 3)
        self.assertEqual(two_city_scheduling([[1, 10], [2, 20]]), 12)
        self.assertEqual(two_city_scheduling([[10, 1], [20, 2]]), 12)
