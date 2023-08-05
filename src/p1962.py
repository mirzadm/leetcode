"""1962. Remove Stones to Minimize the Total

1 <= piles.length <= 10^5
1 <= piles[i] <= 10^4
1 <= k <= 10^5

Possible solutions
- Find max value, k times. O(kn) ~ O(n^2)
- Use a heap, update max k times. O(klog(n))
"""

from typing import List


def min_stone_sum(piles: List[int], k: int) -> int:
    heap = Heap()
    for num in piles:
        heap.insert(num)
    for _ in range(k):
        if heap.elements[0] == 1:
            break
        heap.elements[0] -= heap.elements[0] // 2
        heap.update_max()
    return sum(heap.elements)


class Heap:
    def __init__(self) -> None:
        self.elements = []

    def insert(self, num: int) -> None:
        self.elements.append(num)
        child_index = len(self.elements) - 1
        parent_index = (
            (child_index - 1) // 2 if child_index % 2 == 1 else (child_index - 2) // 2
        )
        while (parent_index >= 0) and (
            self.elements[child_index] > self.elements[parent_index]
        ):
            # Swap parent and child
            self.elements[parent_index], self.elements[child_index] = (
                self.elements[child_index],
                self.elements[parent_index],
            )
            child_index = parent_index
            parent_index = (
                (child_index - 1) // 2
                if child_index % 2 == 1
                else (child_index - 2) // 2
            )

    def update_max(self) -> None:
        if len(self.elements) == 0:
            return
        parent = 0
        while True:
            odd_child = 2 * parent + 1
            even_child = 2 * parent + 2
            swap_index = parent
            if (
                odd_child < len(self.elements)
                and self.elements[odd_child] > self.elements[parent]
            ):
                swap_index = odd_child
            if (
                even_child < len(self.elements)
                and self.elements[even_child] > self.elements[swap_index]
            ):
                swap_index = even_child
            if swap_index == parent:
                break
            self.elements[parent], self.elements[swap_index] = (
                self.elements[swap_index],
                self.elements[parent],
            )
            parent = swap_index
