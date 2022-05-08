"""Problem 382: Return a random node value from a linked list."""

from random import randrange


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

def get_linked_list_length(head: ListNode) -> int:
    """
    Returns the length of a linked list given a head pointer.
    """
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length

def get_linked_list_node(head: ListNode, index: int) -> ListNode:
    """
    Returns a pointer to node at index (starting from 0).
    """
    while (head is not None) and (index > 0):
        head = head.next
        index -= 1
    if head is None:
        raise RuntimeError(f"Linked list does not have a node at index {index}!")
    return head


def random_node_value(head: ListNode) -> int:
    """
    Returns a random value from a linked list.
    """
    if head is None:
        raise ValueError("Linedlist is empty!")
    length = get_linked_list_length(head)
    random_index = randrange(length)
    random_node_pointer = get_linked_list_node(random_index)
    return random_node_pointer.value
