import bisect
from typing import List


class SummaryRanges:
    """Creates summary ranges for incoming data stream.

    Maintains a disjoint sorted list of interval.
    Example:
        Stream: 1, 4, 3, 6, 2, ...
        Dijoint intervals:
            [[1, 1]]
            [[1, 1], [4, 4]]
            [[1, 1], [3, 4]]
            [[1, 1], [3, 4], [6, 6]]
            [[1, 4], [6, 6]]
    """
    def __init__(self):
        self.intervals = []

    def add_value(self, val: int) -> None:
        """Updates summary intervals by adding a new value from stream.

        This could result in:
            - Creating a new interval
            - Extending an existing interval
            - Merging two adjacent intervals
        Args:
            `val`: New integer value from stream.
        """
        if not self.intervals:
            self.intervals = [[val, val]]
        else:
            right_index = self.find_insertion_index(val)
            left_index = right_index - 1
            if right_index == 0:
                if val < self.intervals[right_index][0] - 1:
                    self.intervals.insert(0, [val, val])
                elif val == self.intervals[right_index][0] - 1:
                    self.intervals[right_index][0] = val
            elif right_index == len(self.intervals):
                if val > self.intervals[left_index][1] + 1:
                    self.intervals.append([val, val])
                elif val == self.intervals[left_index][1] + 1:
                    self.intervals[left_index][1] = val
            else:
                if (
                    val > self.intervals[left_index][1] + 1
                    and val < self.intervals[right_index][0] - 1
                ):
                    self.intervals.insert(right_index, [val, val])
                elif (
                    val > self.intervals[left_index][1] + 1
                    and val == self.intervals[right_index][0] - 1
                ):
                    self.intervals[right_index][0] = val
                elif (
                    val == self.intervals[left_index][1] + 1
                    and val < self.intervals[right_index][0] - 1
                ):
                    self.intervals[left_index][1] = val
                elif (
                    val == self.intervals[left_index][1] + 1
                    and val == self.intervals[right_index][0] - 1
                ):
                    self.intervals[left_index][1] = self.intervals[right_index][1]
                    self.intervals.pop(right_index)

    def find_insertion_index(self, val: int) -> int:
        intervals_first_indices = [interval[0] for interval in self.intervals]
        return bisect.bisect(intervals_first_indices, val)

    def get_intervals(self) -> List[List[int]]:
        return self.intervals
