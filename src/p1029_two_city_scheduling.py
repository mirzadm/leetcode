"""Problem 1029: Two City Scheduling."""

from typing import List


def two_city_scheduling(costs: List[List[int]]) -> int:
    """Calculates the min cost for two city scheduling problem.

    Args:
        `costs`: List of 2-element lists representing costs for each city for
        for each candidate. Must includes even number of cost pairs.
    Returns:
        Min cost to assign candidates to cities.
    """
    sorted_costs = sorted(costs, key=lambda item: item[0] - item[1])
    min_cost = 0
    for i in range(len(costs)):
        if i < len(costs) / 2:
            min_cost += sorted_costs[i][0]
        else:
            min_cost += sorted_costs[i][1]
    return min_cost
