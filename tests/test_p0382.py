import pytest
from src.p0382_linked_list_random import (
    ListNode,
    get_linked_list_length,
    get_linked_list_node,
    random_node_value,
)


def test_get_linked_list_length():
    assert get_linked_list_length(None) == 0
    head = ListNode(10)
    assert get_linked_list_length(head) == 1
    head = ListNode(10)
    head.next = ListNode(20)
    assert get_linked_list_length(head) == 2


def test_get_linked_list_node():
    with pytest.raises(RuntimeError):
        get_linked_list_node(None, 0)
    head = ListNode(10)
    assert get_linked_list_node(head, 0) == head
    with pytest.raises(RuntimeError):
        get_linked_list_node(head, 1)
    head = ListNode(10)
    head.next = ListNode(20)
    assert get_linked_list_node(head, 0) == head
    assert get_linked_list_node(head, 1) == head.next
    with pytest.raises(RuntimeError):
        get_linked_list_node(head, 2)


def test_random_node_value():
    with pytest.raises(ValueError):
        random_node_value(None)
    head = ListNode(10)
    assert random_node_value(head) == 10
    head = ListNode(10)
    head.next = ListNode(20)
    assert random_node_value(head) in (10, 20)