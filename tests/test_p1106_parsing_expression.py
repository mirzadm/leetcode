import unittest

from src.p1106_parsing_expression import (
    calculate_boolean_operation as calc,
    parse_boolean_expr as parse,
)


class TestCases(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc("!", ["f"]), "t")
        self.assertEqual(calc("!", ["t"]), "f")
        self.assertEqual(calc("&", ["f", "f"]), "f")
        self.assertEqual(calc("&", ["f", "t"]), "f")
        self.assertEqual(calc("&", ["t", "f"]), "f")
        self.assertEqual(calc("&", ["t", "t"]), "t")
        self.assertEqual(calc("&", ["t", "t", "f"]), "f")
        self.assertEqual(calc("|", ["f", "f"]), "f")
        self.assertEqual(calc("|", ["f", "t"]), "t")
        self.assertEqual(calc("|", ["t", "f"]), "t")
        self.assertEqual(calc("|", ["t", "t"]), "t")
        self.assertEqual(calc("|", ["f", "f", "t"]), "t")

    def test_parse(self):
        self.assertTrue(parse("t"))
        self.assertFalse(parse("f"))

        self.assertFalse(parse("!(t)"))
        self.assertTrue(parse("!(f)"))

        self.assertFalse(parse("&(f,f)"))
        self.assertFalse(parse("&(f,t)"))
        self.assertFalse(parse("&(t,f)"))
        self.assertTrue(parse("&(t,t)"))

        self.assertFalse(parse("|(f,f)"))
        self.assertTrue(parse("|(f,t)"))
        self.assertTrue(parse("|(t,f)"))
        self.assertTrue(parse("|(t,t)"))

        self.assertTrue("&(!(!(t)), !(|(f, f)), t)")
