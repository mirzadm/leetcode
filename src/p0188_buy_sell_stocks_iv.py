"""Problem 188. Best Time to Buy and Sell Stock IV."""

from typing import List, Tuple


def max_profit_dynamic_prog(max_transactions: int, prices: List[int]) -> int:
    """Calculates max profit in buying and selling stocks.

    Uses dynamic programming.

    Restrictions:
        1- Number of transactions <= `max_transactions`
        1- No more than one transaction per day
        2- Must sell before buying new stocks

    Args:
        `price`: List of daily stock prices.
    Returns:
        Max profit in buying and selling stocks.
    """
    price_intervals = parse_intervals(prices)
    if len(price_intervals) == 0 or max_transactions == 0:
        return 0
    if len(price_intervals) < max_transactions:
        max_transactions = len(price_intervals)
    return max_profit_dp_helper(max_transactions, price_intervals)


def max_profit_dp_helper(
    max_transactions: int, price_intervals: List[Tuple[int]]
) -> int:
    """Helper to calculate max profit in buying and selling stocks."""
    curr_profits = {}
    next_profits = {}
    k = 0
    while k < max_transactions:
        for left in range(len(price_intervals)):
            max_profit = 0
            for right in range(left, len(price_intervals)):
                if price_intervals[right][1] > price_intervals[left][0]:
                    profit = price_intervals[right][1] - price_intervals[left][0]
                    if k > 1:
                        if right + 1 in curr_profit:
                            profit += curr_profit[right + 1]
                    if profit > max_profit:
                        max_profit = profit
            next_profits[left] = max_profit
        curr_profits = next_profits
        next_profits = {}
        k += 1
    return max(curr_profits.values())


def max_profit(max_transactions: int, prices: List[int]) -> int:
    """Calculates max profit in buying and selling `max_transactions` stocks.

    Restrictions:
        1- Number of transactions <= `max_transactions`
        1- No more than one transaction per day
        2- Must sell before buying new stocks

    Args:
        `price`: List of daily stock prices.
    Returns:
        Max profit in buying and selling stocks.
    """
    price_intervals = parse_intervals(prices)
    if len(price_intervals) == 0 or max_transactions == 0:
        return 0
    if len(price_intervals) < max_transactions:
        max_transactions = len(price_intervals)
    return max_profit_helper(max_transactions, price_intervals)


def max_profit_helper(
    max_transactions: int, price_intervals: List[Tuple[int]]
) -> int:
    """Helper to calculate max profit in buying and selling stocks."""
    max_profit_value = 0
    for left in range(len(price_intervals) - max_transactions + 1):
        for right in range(left, len(price_intervals) - max_transactions + 1):
            if price_intervals[right][1] > price_intervals[left][0]:
                profit = price_intervals[right][1] - price_intervals[left][0]
                if max_transactions > 1:
                    profit += max_profit_helper(
                        max_transactions - 1, price_intervals[right + 1:]
                    )
                if profit > max_profit_value:
                    max_profit_value = profit
    return max_profit_value


def parse_intervals(prices: List[int]) -> List[Tuple[int]]:
    """Parses prices into ascending price intervals."""
    i = 0
    price_intervals = []
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        left = i
        while i < len(prices) - 1 and prices[i] < prices[i + 1]:
            i += 1
        right = i
        if left < right:
            price_intervals.append((prices[left], prices[right]))
    return price_intervals
