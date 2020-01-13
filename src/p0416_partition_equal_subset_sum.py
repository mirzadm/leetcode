"""Problem 416. Partition Equal Subset Sum"""

from collections import defaultdict
from typing import List

def partition_equal_subset_sum(nums: List[int]) -> bool:
    """Checks if array can be partitioned into two subsets of equal sum.

    Each of the array elements will not exceed 100.
    The array size will not exceed 200.

    Args:
        `nums`: List of positive integers.
    Returns:
        True if there is a way to partition the list otherwise false.
    """
    total = sum(nums)
    if total == 0 or total % 2 == 1:
        return False
    partition_a = defaultdict(int)
    partition_b = defaultdict(int)
    for num in nums:
        partition_a[num] += 1;
    sum_a = total
    sum_b = 0
    states = set()
    while (sum_a != sum_b and sum_a not in states and sum_b not in states):
        states.update((sum_a, sum_b))
        if sum_a > sum_b:
            next_element = find_nearest_element(partition_a, (sum_a - sum_b) / 2)
            partition_a[next_element] -= 1
            partition_b[next_element] += 1
            sum_a -= next_element
            sum_b += next_element
        else:
            next_element = find_nearest_element(partition_b, (sum_b - sum_a) / 2)
            partition_b[next_element] -= 1
            partition_a[next_element] += 1
            sum_b -= next_element
            sum_a += next_element
    return sum_a == sum_b


def find_nearest_element(partition: defaultdict, target: int) -> int:
    """Finds the closest element to `target` in `subset`."""
    i = 0
    while True:
        if target + i <= 100 and partition[target + i] > 0:
            return target + i
        if target - i >= 1 and partition[target - i] > 0:
            return target - i
        i += 1
