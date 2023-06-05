"""Problem 908: Smallest Range I

Find the smallest range in an arry of numbers by modifying each element by a number in [-k, k].
"""

from typing import List

def smallest_range(nums: List[int], k: int) -> int:
    potential_smallest_range = (max(nums) - k) - (min(nums) + k)
    if potential_smallest_range > 0:
        return potential_smallest_range
    else:
        return 0
