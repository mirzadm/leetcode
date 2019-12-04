"""Problem 188. Best Time to Buy and Sell Stock."""

from typing import List


def max_profit(prices: List[int]) -> int:
    """Calculates max profit in buying and selling stocks.

    Restrictions:
        1- One transaction per day
        2- Must sell before buying new stocks

    Args:
        `prices`: List of daily stock prices.
    Returns:
        Max profit in buying and selling stocks.
    """
    if not prices:
        return 0
    left = 0
    i = 0
    profit = 0
    while True:
        while i < len(prices) - 1 and prices[i] > prices[i + 1]:
            i += 1
        if i == len(prices) - 1:
            break
        left = i
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        profit += prices[i] - prices[left]
        if i == len(prices) - 1:
            break
    return profit
