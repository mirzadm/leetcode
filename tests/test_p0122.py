import unittest
from src.p0122_buy_sell_stocks import max_profit


class TestCases(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([]), 0)
        self.assertEqual(max_profit([1]), 0)
        self.assertEqual(max_profit([1, 1]), 0)
        self.assertEqual(max_profit([1, 2]), 1)
        self.assertEqual(max_profit([2, 1]), 0)
        self.assertEqual(max_profit([1, 2, 3]), 2)
        self.assertEqual(max_profit([3, 2, 1]), 0)
        self.assertEqual(max_profit([3, 2, 4]), 2)
        self.assertEqual(max_profit([2, 4, 3]), 2)
        self.assertEqual(max_profit([2, 4, 4]), 2)
        self.assertEqual(max_profit([2, 2, 4]), 2)
        self.assertEqual(max_profit([2, 4, 1, 5]), 6)
        self.assertEqual(max_profit([2, 4, 4, 5]), 3)
        self.assertEqual(max_profit([4, 2, 1, 5]), 4)
