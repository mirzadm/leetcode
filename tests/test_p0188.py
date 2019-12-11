import unittest

from src.p0188_buy_sell_stocks_iv import (
    max_profit, max_profit_dynamic_prog as max_profit_dp
)


class TestCases(unittest.TestCase):
    def test_max_profit_dp(self):
        self.assertEqual(max_profit_dp(1, []), 0)
        self.assertEqual(max_profit_dp(0, [1, 2]), 0)
        self.assertEqual(max_profit_dp(1,[1]), 0)
        self.assertEqual(max_profit_dp(2, [1]), 0)
        self.assertEqual(max_profit_dp(1, [1, 2]), 1)
        self.assertEqual(max_profit_dp(2, [1, 2]), 1)
        self.assertEqual(max_profit_dp(1, [2, 1]), 0)
        self.assertEqual(max_profit_dp(2, [2, 1]), 0)
        self.assertEqual(max_profit_dp(1, [1, 2, 1, 5]), 4)
        self.assertEqual(max_profit_dp(2, [1, 2, 1, 5]), 5)
        self.assertEqual(max_profit_dp(1, [1, 3, 2, 5]), 4)
        self.assertEqual(max_profit_dp(2, [1, 3, 2, 5]), 5)
        self.assertEqual(max_profit_dp(1, [1, 3, 2, 5]), 4)
        self.assertEqual(max_profit_dp(2, [1, 3, 2, 5]), 5)
        self.assertEqual(max_profit_dp(2, [0,8,5,7,4,7]), 11)

    def test_max_profit(self):
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
