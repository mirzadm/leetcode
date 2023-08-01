"""665. Non-decreasing Array

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""

from typing import List


def is_convertible_to_non_decreasing_array(nums: List[int]) -> bool:
    decrease_points = _find_decrease_points(nums)
    if len(decrease_points) == 2:
        return False
    if len(decrease_points) == 0:
        return True
    left = decrease_points[0]
    right = left + 1
    if (left == 0) or (right == len(nums) - 1):
        return True
    if (nums[left - 1] <= nums[right]) or (nums[left] <= nums[right + 1]):
        return True
    return False


def _find_decrease_points(nums: List[int]) -> List[int]:
    decrease_points = []
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            decrease_points.append(i)
            if len(decrease_points) > 1:
                break
    return decrease_points
