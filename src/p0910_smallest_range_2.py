"""Problem 910: Smallest range II."""

from typing import List


def smallest_range_2(nums: List[int], k: int) -> int:
    """
    Find smallest possible range when each number in the nums can be
    replaces by either number + k or number - k.

    Solution assumes an optimal min-max so far and updates them with each new number.
    """
    nums_min = min(nums)
    current_min = nums_min + k
    current_max = nums_min + k
    for num in nums:
        # Only a num that extends the range is to be reckon with!
        if num + k > current_max:
            if num - k < current_min:
                # num extends the range
                # Minimize how much the range is extended by num
                if num + k - current_max > current_min - (num - k):
                    current_min = num - k
                else:
                    current_max = num + k
            elif num - k > current_max:
                current_max = num - k
    return current_max - current_min
