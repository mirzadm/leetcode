"""Problem 15: Find all unique triplets in the array where sum(triplet) = 0."""

from collections import defaultdict
from typing import List


def sum_of_three_n2_partition(nums: List[int]) -> List[List[int]]:
    """Finds all unique triplets in `nums` where sum(triplet) is zero.

    An O(n^2) solution that relies to partitioning numbers into positive and
    negative sublists. It therefore improves time complexity for cases where
    number of positive numbers is considerably larger than negative numbers or
    vice versa.

    Args:
        `nums`: List of integers.
    Returns:
        List of triples which are 3-element lists.
    """
    if len(nums) < 3:
        return []
    counts = defaultdict(int)
    positives = []
    negatives = []
    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        counts[num] += 1
    triplets = set()
    for neg in negatives:
        for pos in positives:
            lookup_value = -(neg + pos)
            if lookup_value in counts:
                # Account for potential repeated values
                # For instance given: lookup_value = -(-2 + 4) = -2
                # Make sure there are at least two -2's in input numbers.
                if (
                    lookup_value not in (neg, pos)
                    or lookup_value == neg and counts[neg] >= 2
                    or lookup_value == pos and counts[pos] >= 2
                ):
                    triplet = tuple(sorted((lookup_value, neg, pos)))
                    triplets.add(triplet) # Only unique triplets
    # Handle the case for (0, 0, 0) triplet separately
    if 0 in counts and counts[0] >= 3:
        triplets.add((0, 0, 0))
    triplets_list = [list(t) for t in triplets]
    return triplets_list
