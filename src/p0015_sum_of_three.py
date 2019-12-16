"""Problem 15: Find all unique triplets in the array where sum(triplet) = 0."""

from collections import defaultdict
from typing import List


def sum_of_three_brute_force(nums: List[int]) -> List[List[int]]:
    triplets = []
    if len(nums) < 3:
        return []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sorted_triplet = sorted([nums[i], nums[j], nums[k]])
                    if sorted_triplet not in triplets:
                        triplets.append(sorted_triplet)
    return triplets


def sum_of_three_n2(nums):
    if len(nums) < 3:
        return []
    sum_to_pairs = defaultdict(set)
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            t = tuple(sorted((nums[i], nums[j])))
            sum_to_pairs[nums[i] + nums[j]].add(t)
    triplets = set()
    for num in nums:
        if -num in sum_to_pairs:
            for pair in sum_to_pairs[-num]:
                if (
                    num not in pair
                    or (num in pair and num != 0 and counts[num] > 1)
                    or (num in pair and num == 0 and counts[0] >= 3)
                ):
                    triplet = tuple(sorted((num, *pair)))
                    triplets.add(triplet)
    triplets_list = [list(t) for t in triplets]
    return triplets_list


def sum_of_three_n2_sorted(nums):
    if len(nums) < 3:
        return []
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    nums.append(0)
    nums = sorted(nums)
    first_zero = nums.index(0)
    positives = nums[first_zero + 1:]
    negatives = nums[: first_zero]
    triplets = set()
    for neg in negatives:
        for pos in positives:
            lookup_value = -(neg + pos)
            if lookup_value in counts:
                if (
                    lookup_value not in (neg, pos)
                    or lookup_value == neg and counts[neg] >= 2
                    or lookup_value == pos and counts[pos] >= 2
                ):
                    triplet = tuple(sorted((lookup_value, neg, pos)))
                    triplets.add(triplet)
    if 0 in counts and counts[0] >= 3:
        triplets.add((0, 0, 0))
    triplets_list = [list(t) for t in triplets]
    return triplets_list
