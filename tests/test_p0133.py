"""Unit tests for problem 133."""

import pytest
from src.p0133_clone_graph import Node, bfs_traversal, clone_graph


def test_bfs_traversal():
    assert bfs_traversal(None) == []
    n1 = Node(1)
    assert bfs_traversal(n1) == [n1]
    n2 = Node(2)
    n3 = Node(3)
    n1 = Node(1, [n2, n3])
    n2.neighbors = [n1]
    n3.neighbors = [n1]
    assert bfs_traversal[n1] == [n1, n2, n3]
    assert bfs_traversal[n2] == [n2, n1, n3]
    assert bfs_traversal[n3] == [n3, n1, n2]

def _test_graph_traversals(first_bfs, second_bfs):
    """Check if traversals are identically-valued
    sequences of node and their neighbors.
    """
    first_graph_value_serialized = [
        (node.val, [neighbor.val for neighbor in node.neighbors]) for node in first_bfs
    ]
    second_graph_value_serialized = [
        (node.val, [neighbor.val for neighbor in node.neighbors]) for node in second_bfs
    ]
    assert first_graph_value_serialized == second_graph_value_serialized

def _test_graph_disjointness(first_bfs, second_bfs):
    """Check if two graphs do not share any nodes."""
    assert set(first_bfs).intersection(set(second_bfs)) == {}

def test_clone_graph():
    assert clone_graph(None) == None
    # 1 node
    n1 = Node(1)
    n1_cloned = clone_graph(n1)
    bfs = bfs_traversal(n1)
    clone_bfs = bfs_traversal(n1_cloned)
    _test_graph_traversals(bfs, clone_bfs)
    _test_graph_disjointness(bfs, clone_bfs)
    # 3 nodes
    n2 = Node(2)
    n3 = Node(3)
    n1 = Node(1, [n2, n3])
    n2.neighbors = [n1]
    n3.neighbors = [n1]
    n1_cloned = clone_graph(n1)
    bfs = bfs_traversal(n1)
    clone_bfs = bfs_traversal(n1_cloned)
    _test_graph_traversals(bfs, clone_bfs)
    _test_graph_disjointness(bfs, clone_bfs)
