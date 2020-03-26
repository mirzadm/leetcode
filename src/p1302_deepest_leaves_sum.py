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
    if not root:
        return None
    nodes = tree_to_full_list(root)
    deepest_level_count = 2 ** math.floor(math.log2(len(nodes)))
    result = sum(
        node.val for node in nodes[-deepest_level_count:] if node is not None
    )
    return result


def tree_to_full_list(root: TreeNode) -> List[TreeNode]:
    if not root:
        return []
    q = deque()
    q.append(root)
    result = []
    deeper_level = True
    level_length = 1
    while deeper_level:
        level = []
        for _ in range(level_length):
            level.append(q.popleft())
        level_length *= 2
        if any(level):
            result.extend(level)
            for node in level:
                if node is None:
                    q.extend([None, None])
                else:
                    q.extend([node.left, node.right])
        else:
            deeper_level = False
    return result
