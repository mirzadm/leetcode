from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def add_num(self, val: int) -> None:
        if not self.intervals:
            self.intervals.append([val, val])
        else:
            right_index = self.find_right_interval_index(val)
            if right_index is None:
                left_index = len(self.intervals) - 1
                if val > self.intervals[left_index][1] + 1:
                    self.intervals.append([val, val])
                elif val == self.intervals[left_index][1] + 1:
                    self.intervals[left_index][1] = val
            elif right_index == 0:
                if val < self.intervals[right_index][0] - 1:
                    self.intervals.insert(0, [val, val])
                elif val == self.intervals[right_index][0] - 1:
                    self.intervals[right_index][0] = val
            else:
                left_index = right_index - 1
                if val > self.intervals[left_index][1] + 1 and val < self.intervals[right_index][0] - 1:
                    self.intervals.insert(right_index, [val, val])
                elif val > self.intervals[left_index][1] + 1 and val == self.intervals[right_index][0] - 1:
                    self.intervals[right_index][0] = val
                elif val == self.intervals[left_index][1] + 1 and val < self.intervals[right_index][0] - 1:
                    self.intervals[left_index][1] = val
                elif val == self.intervals[left_index][1] + 1 and val == self.intervals[right_index][0] - 1:
                    self.intervals[left_index][1] = self.intervals[right_index][1]
                    self.intervals.pop(right_index)

    def find_right_interval_index(self, val: int) -> int:
        for index in range(len(self.intervals)):
            if val < self.intervals[index][0]:
                return index
        return None

    def get_intervals(self) -> List[List[int]]:
        return self.intervals
