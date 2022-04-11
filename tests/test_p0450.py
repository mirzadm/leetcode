"""Tests for problem 450."""

import pytest
from src.p0450_delete_bst_node import TreeNode, BinSearchTree


@pytest.fixture
def create_bin_search_tree():
    bst = BinSearchTree(TreeNode(10))
    bst.root.left = TreeNode(7)
    bst.root.right = TreeNode(12)
    bst.root.left.right = TreeNode(9)
    bst.root.left.right.left = TreeNode(8)
    return bst

def test_delete_root(create_bin_search_tree):
    bst = create_bin_search_tree
    bst.delete_key(10)
    assert bst.root.key == 9
    assert bst.root.left.key == 7
    assert bst.root.left.left == None
    assert bst.root.left.right.key == 8
    assert bst.root.left.right.left == None
    assert bst.root.left.right.right == None
    assert bst.root.right.key == 12
    assert bst.root.right.left == None
    assert bst.root.right.right == None

def test_delete_leaf(create_bin_search_tree):
    bst = create_bin_search_tree
    bst.delete_key(12)
    assert bst.root.key == 10
    assert bst.root.left.key == 7
    assert bst.root.left.left == None
    assert bst.root.left.right.key == 9
    assert bst.root.left.right.left.key == 8
    assert bst.root.left.right.left.left == None
    assert bst.root.left.right.left.right == None
    assert bst.root.left.right.right == None
    assert bst.root.right == None

def test_delete_nonroot_with_right_only_child(create_bin_search_tree):
    bst = create_bin_search_tree
    bst.delete_key(7)
    assert bst.root.key == 10
    assert bst.root.left.key == 8
    assert bst.root.left.left == None
    assert bst.root.left.right.key == 9
    assert bst.root.left.right.left == None
    assert bst.root.left.right.right == None
    assert bst.root.right.key == 12
    assert bst.root.right.left == None
    assert bst.root.right.right == None
