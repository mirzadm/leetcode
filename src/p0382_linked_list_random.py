"""Problem 382: Return a random node's value from a linked list."""

from random import randrange


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class RandomNode:
    def __init__(self, head: ListNode):
        self.head = head

    def random_node(self, rand_func=randrange) -> int:
        """Returns a random value from linked list.

        Args:
            `rand_func`: Optional random generator function as an argument.
                It allows for mocking the random generator in unit testing.
        Returns:
            Random value from linked list (integer).
        """
        faster = self.head
        slower = self.head
        k = 0
        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next
            k += 1
        if faster is None:
            n = 2 * k
        else:
            n = 2 * k + 1
        random_index = rand_func(n)
        if random_index <= n / 2:
            pointer = self.head
        else:
            pointer = slower
            random_index -= n / 2
        i = 0
        while i < random_index:
            pointer = pointer.next
            i += 1
        return pointer.value
