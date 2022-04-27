"""Given a binary tree, return the sum of values of its deepest leaves."""

import math
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def deepest_leaves_sum(root: TreeNode) -> int:
    """
    Returns the sum of leaf node values at the lowest level in a binary tree.

    Uses a modified breadth-first-search traversal that queues a (depth, node) tuple
    for each new node.
    """
    if not root:
        return None
    bfs_queue = deque() # A queue to push/pop nodes in breadth-first-search order
    current_depth = 0 # Current tree depth
    current_depth_sum = 0 # Sum of node values in the current depth
    bfs_queue.appendleft((0, root))
    while bfs_queue:
        depth, node = bfs_queue.pop()
        if depth != current_depth:
            current_depth_sum = node.val
            current_depth = depth
        else:
            current_depth_sum += node.val
        if node.left:
            bfs_queue.appendleft((current_depth + 1, node.left))
        if node.right:
            bfs_queue.appendleft((current_depth + 1, node.right))
    return current_depth_sum
