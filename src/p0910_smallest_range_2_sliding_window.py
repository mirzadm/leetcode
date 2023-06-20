"""Problem 910: Smallest range II.

Given a list of numbers and a value k, where each number can only be modified to num-k or num+k,
find the smallest range.

Constraints:
    0 <= len(nums) <= 10,000
    0 <= num <= 10,000
    0 <= k <= 10,000

Insights
- If k >= initial range of numbers, the best we could do is the initial range.
- This problem cannot be solved by simple iteration e.g. deciding on -k or +k one number
  at a time leads to sub-optimal solution. Same for iterating from left and right.

Solutions
- Exponential: trying each combination -/+k for every number: 2^10,000 (~ 10^3000) combinations to check
- Sliding window
    Generate -/+k offsets for all numbers
    Sort the result
    Use a sliding window algorithm to find smallest window that covers one varations of every number
- Partition
    Start with the shape of the solution. The sorted list of number will have a left partion
    where every number is +k and a right partition where every number is -k.
    Examine all patitions and find the one that gives smallest range.
"""

from typing import List, Tuple, Set, Optional, NamedTuple


class NumShiftedNumPair(NamedTuple):
    num: int
    shifted_num: int


def smallest_range_2_sliding_window(nums: List[int], k: int) -> int:
    initial_min, initial_max = min(nums), max(nums)
    initial_range = initial_max - initial_min
    if k >= initial_range:
        return initial_range
    unique_nums = set(nums)
    num_shifted_pairs = _create_num_shifted_pairs(
        unique_nums, k, initial_min, initial_max
    )
    num_shifted_pairs.sort(key=lambda t: t.shifted_num)
    smallest_range = initial_range
    unique_nums_len = len(unique_nums)
    covered_nums = set()
    left = right = 0
    while True:
        left, right = _get_next_minimal_covering_range(
            num_shifted_pairs, unique_nums_len, left, right, initial_min, covered_nums
        )
        new_range = (
            num_shifted_pairs[right].shifted_num - num_shifted_pairs[left].shifted_num
        )
        if new_range < smallest_range:
            smallest_range = new_range
        if (
            num_shifted_pairs[left].num != initial_min
            and right < len(num_shifted_pairs) - 1
        ):
            covered_nums.remove(num_shifted_pairs[left].num)
            left += 1
            right += 1
        else:
            break
    return smallest_range


def _get_next_minimal_covering_range(
    num_shifted_pairs: List[NumShiftedNumPair],
    unique_nums_len: int,
    left: int,
    right: int,
    initial_min: int,
    covered_nums: Set[int],
) -> Tuple[Optional[int], Optional[int]]:
    """
    Given a range (left-->right) that partially covers numbers,
    find the next minimal range to the right that covers all numbers.
    """
    while True:
        if num_shifted_pairs[right].num in covered_nums:
            if num_shifted_pairs[left].num != initial_min:
                left += 1
        else:
            covered_nums.add(num_shifted_pairs[right].num)
            if len(covered_nums) == unique_nums_len:
                break
        right += 1
    return left, right


def _create_num_shifted_pairs(
    nums: Set[int], k: int, initial_min: int, initial_max: int
) -> List[NumShiftedNumPair]:
    pairs = []
    for num in nums:
        if num == initial_min:
            pairs.append(NumShiftedNumPair(num, num + k))
        elif num == initial_max:
            pairs.append(NumShiftedNumPair(num, num - k))
        else:
            pairs.extend(
                [NumShiftedNumPair(num, num - k), NumShiftedNumPair(num, num + k)]
            )
    return pairs
