import unittest

from src.p0352_disjoint_intervals_summary import SummaryRanges


class CustomTestCase(unittest.TestCase):

    def test_summary_ranges(self):
        summary_ranges = SummaryRanges()
        summary_ranges.add_num(3)
        self.assertEqual(summary_ranges.get_intervals(), [[3, 3]])
        summary_ranges.add_num(3)
        self.assertEqual(summary_ranges.get_intervals(), [[3, 3]])
        summary_ranges.add_num(2)
        self.assertEqual(summary_ranges.get_intervals(), [[2, 3]])
        summary_ranges.add_num(4)
        self.assertEqual(summary_ranges.get_intervals(), [[2, 4]])
        summary_ranges.add_num(6)
        self.assertEqual(summary_ranges.get_intervals(), [[2, 4], [6, 6]])
        summary_ranges.add_num(5)
        self.assertEqual(summary_ranges.get_intervals(), [[2, 6]])
        summary_ranges.add_num(0)
        self.assertEqual(summary_ranges.get_intervals(), [[0, 0], [2, 6]])
        summary_ranges.add_num(1)
        self.assertEqual(summary_ranges.get_intervals(), [[0, 6]])
