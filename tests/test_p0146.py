import unittest
from src.p0146_lru_cache import LRUCache


class TestCases(unittest.TestCase):
    def test_lru_cache(self):
        with self.assertRaises(RuntimeError):
            c = LRUCache(0)
        c = LRUCache(2)
        c.put(1, "A")
        c.put(2, "B")
        self.assertEqual(c.get(1), "A")
        c.put(3, "C")
        self.assertEqual(c.get(1), "A")
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(3), "C")
