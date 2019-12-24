import unittest
from src.p0382_linked_list_random import ListNode, RandomNode


class TestCases(unittest.TestCase):
    def setUp(self):
        self.one_element = RandomNode(ListNode(1))
        n = ListNode(1)
        n.next = ListNode(2)
        self.two_element = RandomNode(n)

    def test_random_node(self):
        self.assertEqual(self.one_element.random_node(), 1)
        self.assertEqual(self.two_element.random_node(rand_func=lambda x: 0), 1)
        self.assertEqual(self.two_element.random_node(rand_func=lambda x: 1), 2)
