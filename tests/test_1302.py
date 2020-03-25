import unittest
from src.p1302_deepest_leaves_sum import (
    TreeNode as Node,
    deepest_leaves_sum,
)


class TestCases(unittest.TestCase):
    def test_deepest_leaves_sum(self):
        self.assertIsNone(deepest_leaves_sum(None))

        n = Node(1)
        self.assertEqual(deepest_leaves_sum(n), 1)

        n = Node(1)
        n.left = Node(2)
        self.assertEqual(deepest_leaves_sum(n), 2)

        n = Node(1)
        n.right = Node(3)
        self.assertEqual(deepest_leaves_sum(n), 3)

        n = Node(1)
        n.left = Node(2)
        n.right = Node(3)
        self.assertEqual(deepest_leaves_sum(n), 5)

        n = Node(1)
        n.left = Node(2)
        n.right = Node(3)
        n.left.left = Node(4)
        n.right.right = Node(7)
        self.assertEqual(deepest_leaves_sum(n), 11)
