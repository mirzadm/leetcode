"""Unit tests for problem 1302"""

from src.p1302_deepest_leaves_sum import (
    TreeNode as Node,
    deepest_leaves_sum,
)


def test_deepest_leaves_sum():
    n = Node(1)
    assert deepest_leaves_sum(n) == 1

    n = Node(1)
    n.left = Node(2)
    assert deepest_leaves_sum(n) == 2

    n = Node(1)
    n.right = Node(3)
    assert deepest_leaves_sum(n) == 3

    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    assert deepest_leaves_sum(n) == 5

    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.left.left = Node(4)
    n.right.right = Node(7)
    assert deepest_leaves_sum(n) == 11

    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.right.left = Node(7)
    assert deepest_leaves_sum(n) == 7
