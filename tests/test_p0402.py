import unittest
from src.p0402_remove_k_digits import (
    remove_k_digits as digits_n,
    remove_k_digits_n2 as digits_n2,
)

class TestCases(unittest.TestCase):
    # Test cases for O(n) solution
    def test_digits_n_exception(self):
        self.assertRaises(IndexError, digits_n, "1", 2)
        self.assertRaises(IndexError, digits_n, "12", -1)

    def test_digits_n_expected(self):
        self.assertEqual(digits_n("1", 0), "1")
        self.assertEqual(digits_n("1", 1), "0")

        self.assertEqual(digits_n("12", 0), "12")
        self.assertEqual(digits_n("12", 1), "1")
        self.assertEqual(digits_n("21", 1), "1")
        self.assertEqual(digits_n("12", 2), "0")

        self.assertEqual(digits_n("123", 0), "123")
        self.assertEqual(digits_n("123", 1), "12")
        self.assertEqual(digits_n("123", 2), "1")
        self.assertEqual(digits_n("123", 3), "0")

        self.assertEqual(digits_n("321", 0), "321")
        self.assertEqual(digits_n("321", 1), "21")
        self.assertEqual(digits_n("321", 2), "1")
        self.assertEqual(digits_n("321", 3), "0")

    # Test cases for O(n^2) solution
    def test_digits_n2_exception(self):
        self.assertRaises(IndexError, digits_n2, "1", 2)
        self.assertRaises(IndexError, digits_n2, "12", -1)

    def test_digits_n2_expected(self):
        self.assertEqual(digits_n2("1", 0), "1")
        self.assertEqual(digits_n2("1", 1), "0")

        self.assertEqual(digits_n2("12", 0), "12")
        self.assertEqual(digits_n2("12", 1), "1")
        self.assertEqual(digits_n2("21", 1), "1")
        self.assertEqual(digits_n2("12", 2), "0")

        self.assertEqual(digits_n2("123", 0), "123")
        self.assertEqual(digits_n2("123", 1), "12")
        self.assertEqual(digits_n2("123", 2), "1")
        self.assertEqual(digits_n2("123", 3), "0")

        self.assertEqual(digits_n2("321", 0), "321")
        self.assertEqual(digits_n2("321", 1), "21")
        self.assertEqual(digits_n2("321", 2), "1")
        self.assertEqual(digits_n2("321", 3), "0")
