"""Problem 450. Delete a node from a BST."""

from collections import deque
from typing import Tuple, Union, List

class TreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self, root):
        self.root = root

    def _convert_binsearch_list_to_tree(keys: List[int]):
        """Converst a binary search-formatted list to its corresponding binary search tree."""
        if not keys:
            return None
        root = TreeNode(keys[0])
        nodes = deque()
        nodes.appendleft(root)
        for i, key in enumerate(keys):
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            if left_child_index >= len(keys):
                break
            else:
                parent = nodes.pop()
                left_child = TreeNode(keys[left_child_index])
                parent.left = left_child
                nodes.appendleft(left_child)
                if right_child_index < len(keys):
                    right_child = TreeNode(keys[right_child_index])
                    parent.right = right_child
                    nodes.appendleft(right_child)
        del deque
        return root

    def _find_node_and_parent(self, key: int) -> Tuple[Union[TreeNode, None], Union[TreeNode, None]]:
        """Return node containing key and its parent node."""
        parent = None
        current = self.root
        while current:
            if current.key == key:
                return parent, current
            elif current.key > key:
                parent, current = current, current.left
            else:
                parent, current = current, current.right
        return None, None

    def _find_min(self, root: TreeNode) -> Tuple[Union[None, TreeNode], Union[None, TreeNode]]:
        """Return node with min key in subtree at root and its parent node."""
        current = root
        parent = None
        while current:
            if current.left:
                parent, current = current, current.left
            else:
                return parent, current
        return None, None

    def _find_max(self, root: TreeNode) -> Tuple[Union[None, TreeNode], Union[None, TreeNode]]:
        """Return node with max key in subtree at root and its parent node."""
        current = root
        parent = None
        while current:
            if current.right:
                parent, current = current, current.right
            else:
                return parent, current
        return None, None

    def _remove_subtree_root(self, root: TreeNode) -> Union[TreeNode, None]:
        """Given the root of a BST, remove the root and return a new BST root

        It does not "delete" the current root.
        """
        if root is None:
            return None

        new_root = None
        if root.left:
            parent, new_root = self._find_max(root.left)
            if parent is None:
                new_root.right = root.right
            else:
                # If node is max, it must be the right child of its parent
                # and must not have a right child itself
                parent.right = new_root.left
                new_root.left, new_root.right = root.left, root.right
        elif root.right:
            parent, new_root = self._find_min(root.right)
            if parent is None:
                new_root.left = root.left
            else:
                # If node is min it must be the left child of its parent
                # and must not have a left child itself
                parent.left = new_root.right
                new_root.left, new_root.right = root.left, root.right
        return new_root

    def delete_key(self, key: int) -> None:
        """Deletes a key from the BST"""
        parent, node = self._find_node_and_parent(key)
        if node is None:
            return
        new_subtree_root = self._remove_subtree_root(node)
        if node == self.root:
            self.root = new_subtree_root
        elif parent.left == node:
            parent.left = new_subtree_root
        else:
            parent.right = new_subtree_root
        del node
