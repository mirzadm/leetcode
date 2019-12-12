"""Problem 15: Find all unique triplets in the array where sum(triplet) = 0."""

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
