import unittest
from src.p0416_partition_equal_subset_sum import partition_equal_subset_sum as func


class TestCases(unittest.TestCase):
    def test_partition_equal_subset_sum(self):
        self.assertTrue(func([]))
        self.assertFalse(func([1]))
        self.assertTrue(func([1, 1]))
        self.assertTrue(func([1, 2, 1]))
        self.assertFalse(func([1, 3, 2, 1]))
        self.assertFalse(func([1, 2, 3, 5]))
        self.assertTrue(func([1, 5, 11, 5]))
