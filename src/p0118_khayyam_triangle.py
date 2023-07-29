"""Khayyam Triangle"""

from typing import List


def khayyam_triangle(num_rows: int) -> List[List[int]]:
    triangle = [[1]]
    if num_rows == 1:
        return triangle
    for i in range(1, num_rows):
        current_row = [1]
        previous_row = triangle[i - 1]
        for j in range(len(previous_row) - 1):
            current_row.append(previous_row[j] + previous_row[j + 1])
        current_row.append(1)
        triangle.append(current_row)
    return triangle
