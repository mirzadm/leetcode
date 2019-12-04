"""Problem 188. Best Time to Buy and Sell Stock IV."""

from typing import List


def max_profit(max_transactions: int, prices: List[int]) -> int:
    """Calculates max profit in buying and selling `max_transactions` stocks.

    Restrictions:
        1- Number of transactions <= `max_transactions`
        1- No more than one transaction per day
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
    profits = []
    while True:
        while i < len(prices) - 1 and prices[i] > prices[i + 1]:
            i += 1
        if i == len(prices) - 1:
            break
        left = i
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        profits.append(prices[i] - prices[left])
        if i == len(prices) - 1:
            break
    sorted_profits = sorted(profits, reverse=True)
    return sum(sorted_profits[:max_transactions])
