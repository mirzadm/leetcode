"""Problem 2640: Find the Score of All Prefixes of an Array

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from typing import List


def find_prefix_score(nums: List[int]) -> List[int]:
    prefix_score = []
    current_max = 0
    current_sum = 0
    for num in nums:
        if current_max < num:
            current_max = num
        new_conversion = num + current_max
        current_sum += new_conversion
        prefix_score.append(current_sum)
    return prefix_score
