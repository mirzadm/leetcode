"""Problem 910: Smallest range II.

Given a list of numbers and a value k, where each number can only be modified to num-k or num+k, find the smallest range.

Constraints:
    0 <= len(nums) <= 10,000
    0 <= num <= 10,000
    0 <= k <= 10,000

Insights
- If k >= initial range of numbers, the best we could do is the initial range.
- This problem cannot be solved by simple iteration e.g. deciding on -k or +k one number
  at a time leads to sub-optimal solution. Same for iterating from left and right.
- Constraints on the size input are key here.

Solutions
- Exponential: trying each combination -/+k for every number. That is 2^10,000 (~ 10^3000) combinations to check
- Sliding window
    Generate -/+k offsets for all numbers
    Sort the result
    Use a sliding window algorithm to find smallest window that covers one varations of every number

"""

from typing import List, Tuple, Set, Optional, NamedTuple


class NumShiftedNumPair(NamedTuple):
    num: int
    shifted_num: int


def smallest_range_2(nums: List[int], k: int) -> int:
    initial_min, initial_max = min(nums), max(nums)
    initial_range = initial_max - initial_min
    if k >= initial_range:
        return initial_range
    # Remove duplicates
    unique_nums = set(nums)
    num_shifted_pairs = _create_num_shift_pairs(
        unique_nums, k, initial_min, initial_max
    )
    num_shifted_pairs.sort(key=lambda t: t.shifted_num)
    smallest_range = initial_range
    unique_nums_len = len(unique_nums)
    covered_nums = {}
    left_index = right_index = 0
    while True:
        left_index, right_index = _get_next_range(
            num_shifted_pairs, unique_nums_len, left_index, right_index, covered_nums
        )
        if right_index is None:
            break
        new_range = num_shifted_pairs[right_index].shifted_num - num_shifted_pairs[left_index].shifted_num
        if new_range < smallest_range:
            smallest_range = new_range
        left_key = num_shifted_pairs[left_index].num
        covered_nums.pop(left_key)
        left_index += 1
        right_index += 1
    return smallest_range


def _get_next_range(
    num_shifted_pairs: List[NumShiftedNumPair],
    unique_nums_len: int,
    left_index: int,
    right_index: int,
    covered_nums: Set[int],
) -> Tuple[Optional[int], Optional[int]]:
    while right_index < len(num_shifted_pairs):
        right_key = num_shifted_pairs[right_index].num
        if right_key in covered_nums:
            covered_nums[right_key] += 1
        else:
            covered_nums[right_key] = 1
        if len(covered_nums) < unique_nums_len:
            right_index += 1
        else:
            break
    if len(covered_nums) != unique_nums_len:
        return None, None
    while covered_nums[num_shifted_pairs[left_index].num] == 2:
        covered_nums[num_shifted_pairs[left_index].num] = 1
        left_index += 1
    return left_index, right_index


def _create_num_shift_pairs(
    nums: Set[int], k: int, initial_min: int, initial_max: int
) -> List[NumShiftedNumPair]:
    pairs = []
    for num in nums:
        if num == initial_min:
            pairs.append(NumShiftedNumPair(num, num + k))
        elif num == initial_max:
            pairs.append(NumShiftedNumPair(num, num - k))
        else:
            pairs.extend([NumShiftedNumPair(num, num - k), NumShiftedNumPair(num, num + k)])
    return pairs
