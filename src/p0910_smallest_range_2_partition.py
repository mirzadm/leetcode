"""Problem 910: Smallest range II."""

from typing import List


def smallest_range_2_partition(nums: List[int], k: int) -> int:
    nums_min, nums_max = min(nums), max(nums)
    basic_range = nums_max - nums_min
    if k >= basic_range:
        return basic_range
    smallest_range = basic_range
    nums.sort()
    shifted_min = nums_min + k
    shifted_max = nums_max - k
    for i in range(len(nums) - 1):
        parition_range = max(nums[i] + k, shifted_max) - min(
            nums[i + 1] - k, shifted_min
        )
        smallest_range = min(smallest_range, parition_range)
    return smallest_range
