"""Problem 450. Delete a node from a BST."""

from typing import Tuple, Union

class TreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self, root):
        self.root = root

    def find_node_and_parent(self, key: int) -> Tuple[TreeNode, TreeNode]:
        current = self.root
        parent = None
        while current:
            if current.key == key:
                return parent, current
            elif current.key > key:
                parent, current = current, current.left
            else:
                parent, current = current, current.right
        return None, None

    def find_min(self, root: TreeNode) -> Tuple[Union[None, TreeNode], Union[None, TreeNode]]:
        current = root
        parent = None
        while current:
            if current.left:
                parent, current = current, current.left
            else:
                return parent, current
        return None, None

    def find_max(self, root: TreeNode) -> Tuple[Union[None, TreeNode], Union[None, TreeNode]]:
        current = root
        parent = None
        while current:
            if current.right:
                parent, current = current, current.right
            else:
                return parent, current
        return None, None

    def remove_subtree_root(self, root: TreeNode) -> Union[TreeNode, None]:
        """Given the root of a BST, remove the root and return a new BST root

        It does not "delete" the current root.
        """
        if root is None:
            return None

        new_root = None
        if root.left:
            parent, new_root = self.find_max(root.left)
            if parent is None:
                new_root.right = root.right
            else:
                # If node is max, it must be the right child of its parent
                # and must not have a right child itself
                parent.right = new_root.left
                new_root.left, new_root.right = root.left, root.right
        elif root.right:
            parent, new_root = self.find_min(root.right)
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
        parent, node = self.find_node_and_parent(key)
        if node is None:
            return
        new_subtree_root = self.delete_subtree_root(node)
        if node == self.root:
            self.root = new_subtree_root
        elif parent.left == node:
            parent.left = new_subtree_root
        else:
            parent.right = new_subtree_root
        del node
