"""1913. Maximum Product Difference Between Two Pairs"""

from typing import List


def max_product_difference(nums: List[int]) -> int:
    first_max_index = first_min_index = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[first_max_index]:
            first_max_index = i
        elif nums[i] < nums[first_min_index]:
            first_min_index = i

    second_max_index = second_min_index = None
    for i in range(0, len(nums)):
        if i not in (first_max_index, first_min_index):
            if second_max_index is None:
                second_max_index = i
            elif nums[i] > nums[second_max_index]:
                second_max_index = i
            if second_min_index is None:
                second_min_index = i
            elif nums[i] < nums[second_min_index]:
                second_min_index = i

    return (nums[first_max_index] * nums[second_max_index]) - (
        nums[first_min_index] * nums[second_min_index]
    )
