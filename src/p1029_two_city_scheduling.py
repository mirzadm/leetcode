"""Problem 1029: Two City Scheduling."""

from typing import List


def two_city_scheduling(costs: List[List[int]]) -> int:
    """Calculates the min cost for two city scheduling problem.

    Args:
        `costs`: List of cost pairs representing costs for flying a
                 candidate to a each of two cities.
                 Assumes an even number of items in the list.
    Returns:
        Min cost to fly candidates to one of the two cities.
    """
    middle = len(costs) // 2
    sorted_costs = sorted(costs, key=lambda item: item[0] - item[1])
    min_cost = (
        sum(cost_pair[0] for cost_pair in sorted_costs[: middle])
        + sum(cost_pair[1] for cost_pair in sorted_costs[middle:])
    )
    return min_cost
