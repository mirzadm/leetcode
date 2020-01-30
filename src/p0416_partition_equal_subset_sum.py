"""Problem 416. Partition Equal Subset Sum"""

from typing import List, Dict, Tuple


def partition_equal_subset_sum(nums: List[int]) -> bool:
    """Check if `nums` can be partitioned to 2 subsets of equal sum.

    Wraps `can_partition`, initializes `cache`, and takes care of edge cases.
    Each of the array elements will not exceed 100. The array size will not
    exceed 200.

    Args:
        `nums`: List of positive integers.
    Returns:
        True if there is a way to partition the list otherwise False.
    """
    if not nums:
        return True
    nums_sum = sum(nums)
    if nums_sum % 2 == 1:
        return False
    cache = {}
    return can_partition(nums, len(nums) - 1, nums_sum / 2, cache)


def can_partition(
    nums: List[int], length: int, total: int, cache: Dict[Tuple[int, int], bool]
) -> bool:
    """Is there a subset of `nums[:length]` whose sum equals `total`?

    Uses memoization to dynamically store intemediate results in `cache`.

    Args:
        `nums`: List of integers.
        `length`: Length of `nums` to consider.
        `total`: Target sum value.
        `cache`: Dictionary that stores intermediate boolean results.
    Returns:
        True is a subset was found otherwise False.
    """
    if total == 0:
        return True
    if length == 0 or total < 0:
        return False
    if (length, total) not in cache:
        cache[(length, total)] = (
            can_partition(
                nums, length - 1, total - nums[length - 1], cache
            )
            or can_partition(nums, length - 1, total, cache)
        )
    return cache[(length, total)]
