"""Problem 416. Partition Equal Subset Sum"""

from typing import List


def partition_equal_subset_sum(nums: List[int]) -> bool:
    """Checks if array can be partitioned into two subsets of equal sum.

    Each of the array elements will not exceed 100.
    The array size will not exceed 200.

    Args:
        `nums`: List of positive integers.
    Returns:
        True if there is a way to partition the list otherwise false.
    """
    if not nums:
        return True
    nums_sum = sum(nums)
    if nums_sum % 2 == 1:
        return False
    cache = {}
    return can_partition(nums, len(nums) - 1, nums_sum / 2, cache)


def can_partition(nums, last_index, sum_value, cache):
    if sum_value == 0:
        return True
    if last_index < 0 or sum_value < 0:
        return False
    if (last_index, sum_value) not in cache:
        cache[(last_index, sum_value)] = (
            can_partition(nums, last_index - 1, sum_value - nums[last_index], cache
            )
            or can_partition(nums, last_index - 1, sum_value, cache)
        )
    return cache[(last_index, sum_value)]
