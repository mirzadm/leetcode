"""1883. Minimum Skips to Arrive at Meeting On Time"""


from functools import cache
from math import ceil, inf
from typing import List, Tuple

def min_skips(dist: List[int], speed: int, hours_before: int) -> int:
    # Convert to immutable to allow caching
    immutable_dist = tuple(dist)
    for skips in range(len(dist)):
        if min_distance(len(dist), skips, immutable_dist, speed) <= speed * hours_before:
            return skips
    return -1

@cache
def min_distance(n: int, skips: int, dist: Tuple[int], speed: int) -> int:
    """
    Calculate min "equivalent distance" to cross the first n roads
    with k available skips.
    Min "equivalent distance" = (Min time) * speed
    """
    if skips < 0:
        return inf
    if n <= 0:
        return 0
    # The last road is skipped by default
    if n == len(dist):
        return min_distance(n - 1, skips, dist, speed) + dist[n - 1]

    min_distance_with_skip = min_distance(n - 1, skips - 1, dist, speed) + dist[n - 1]

    min_time_without_skip = ceil((min_distance(n - 1, skips, dist, speed) + dist[n - 1]) / speed)
    min_distance_without_skip = min_time_without_skip * speed

    return min(min_distance_with_skip, min_distance_without_skip)
