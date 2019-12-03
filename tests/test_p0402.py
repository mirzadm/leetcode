import unittest
from src.p0402_remove_k_digits import (
    remove_k_digits as digits_n,
    remove_k_digits_n2 as digits_n2,
)

class TestCases(unittest.TestCase):
    # Test cases for O(n) solution
    def test_digits_n_expected(self):
        # Exception
        self.assertRaises(IndexError, digits_n2, "1", 2)
        self.assertRaises(IndexError, digits_n2, "12", -1)

        # Expected
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

        self.assertEqual(digits_n("213", 0), "213")
        self.assertEqual(digits_n("213", 1), "13")
        self.assertEqual(digits_n("213", 2), "1")
        self.assertEqual(digits_n("213", 3), "0")

        self.assertEqual(digits_n("203", 0), "203")
        self.assertEqual(digits_n("203", 1), "3")
        self.assertEqual(digits_n("203", 2), "0")
        self.assertEqual(digits_n("203", 3), "0")

    # Test cases for O(n^2) solution
    def test_digits_n2(self):
        # Exception
        self.assertRaises(IndexError, digits_n2, "1", 2)
        self.assertRaises(IndexError, digits_n2, "12", -1)

        # Expected
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

        self.assertEqual(digits_n("213", 0), "213")
        self.assertEqual(digits_n("213", 1), "13")
        self.assertEqual(digits_n("213", 2), "1")
        self.assertEqual(digits_n("213", 3), "0")

        self.assertEqual(digits_n("203", 0), "203")
        self.assertEqual(digits_n("203", 1), "3")
        self.assertEqual(digits_n("203", 2), "0")
        self.assertEqual(digits_n("203", 3), "0")
