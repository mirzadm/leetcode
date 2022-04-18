"""Unit tests for problem 133."""

import pytest
from src.p0133_clone_graph import Node, graph_to_map, clone_graph


def test_graph_to_map():
    assert graph_to_map(None) == dict()
    n1 = Node(1)
    assert graph_to_map(n1) == {1: n1}
    n2 = Node(2)
    n3 = Node(3)
    n1 = Node(1, [n2, n3])
    n2.neighbors = [n1]
    n3.neighbors = [n1]
    assert graph_to_map[n1] == {1: n1, 2: n2, 3: n3}
    assert graph_to_map[n2] == {1: n1, 2: n2, 3: n3}
    assert graph_to_map[n3] == {1: n1, 2: n2, 3: n3}

def is_correct_clone(orig_graph, cloned_graph):
    """Helper function to compare graph-maps of original and cloned graphs."""
    # Cloned graph must not share any nodes with the original graph
    orig_nodes = set(orig_graph.values())
    cloned_nodes = set(cloned_graph.values())
    if orig_nodes.intersection(cloned_nodes):
        return False
    # Check each nodes neighbors
    orig_node_tuples = sorted(orig_graph.items())
    cloned_node_tuples = sorted(cloned_graph.items())
    for first, second in zip(orig_node_tuples, cloned_node_tuples):
        # Compare keys first
        if first[0] != second[0]:
            return False
        first_neighbor_ids = set(n.val for n in first[1])
        second_neighbor_ids = set(n.val for n in second[1])
        if first_neighbor_ids != second_neighbor_ids:
            return False
    return True

def test_clone_graph():
    assert clone_graph(None) == None
    # 1 node
    n1 = Node(1)
    cloned = clone_graph(n1)
    assert cloned != n1
    assert cloned.neighbors == []
    assert cloned.val == n1.val
    # 3 nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]
    cloned = clone_graph(n1)
    n1_map = graph_to_map(n1)
    cloned_map = graph_to_map(cloned)
    assert is_correct_clone(n1_map, cloned_map) == True
