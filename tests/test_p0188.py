import unittest

from src.p0188_buy_sell_stocks_iv import max_profit


class TestCases(unittest.TestCase):
    def text_max_profit(self):
        self.assertEqual(max_profit(1, []), 0)
        self.assertEqual(max_profit(0, [1, 2]), 0)
        self.assertEqual(max_profit(1,[1]), 0)
        self.assertEqual(max_profit(2, [1]), 0)
        self.assertEqual(max_profit(1, [1, 2]), 1)
        self.assertEqual(max_profit(2, [1, 2]), 1)
        self.assertEqual(max_profit(1, [2, 1]), 0)
        self.assertEqual(max_profit(2, [2, 1]), 0)
        self.assertEqual(max_profit(1, [1, 2, 1, 5]), 4)
        self.assertEqual(max_profit(2, [1, 2, 1, 5]), 5)
        self.assertEqual(max_profit(1, [1, 3, 2, 5]), 4)
        self.assertEqual(max_profit(2, [1, 3, 2, 5]), 5)
        self.assertEqual(max_profit(1, [1, 3, 2, 5]), 4)
        self.assertEqual(max_profit(2, [1, 3, 2, 5]), 5)
