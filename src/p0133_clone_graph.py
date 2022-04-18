"""Problem 133. Clone a graph.

A two step solution:
1- Create a map of the graph
2- Use the map to clone the graph
"""

from typing import Dict, Union
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def graph_to_map(node: Node) -> Dict[int, Node]:
    """Use BFS to create a map of val->Node for the graph.

    Assume unique val for each node.
    """
    graph_map = {}
    if node is None:
        return graph_map
    node_queue = deque()
    node_queue.appendleft(node)
    graph_map[node.val] = node
    while node_queue:
        next_node = node_queue.pop()
        for neighbor in next_node.neighbors:
            if neighbor.val not in graph_map:
                graph_map[neighbor.val] = neighbor
                node_queue.appendleft(neighbor)
    return graph_map

def clone_graph(node: Node) -> Union[None, Dict[int, Node]]:
    """Clone graph."""
    if node is None:
        return None
    graph_map = graph_to_map(node)
    clone_map = {val: Node(val) for val in graph_map}
    for val, orig_node in graph_map.items():
        cloned_node = clone_map[val]
        cloned_node.neighbors = [clone_map[n.val] for n in orig_node.neighbors]
    return clone_map[node.val]