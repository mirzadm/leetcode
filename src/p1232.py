"""1232. Check If It Is a Straight Line


Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates are int
    coordinates contains no duplicate point.
"""

from typing import List


def check_straight_line(coordinates: List[List[int]]) -> bool:
    # Check edge cases: horizontal and vertical lines
    # y = ax + b, a = (y2 - y1)/ (x2 - x1)
    if coordinates[0][0] == coordinates[1][0]:  # Vertical line
        slope = None
        intercept = coordinates[0][0]
    else:
        slope = (coordinates[0][1] - coordinates[1][1]) / (
            coordinates[0][0] - coordinates[1][0]
        )
        intercept = coordinates[0][1] - slope * coordinates[0][0]
    for coordinate in coordinates[2:]:
        if slope is None:
            if coordinate[0] != intercept:
                return False
        else:
            y = slope * coordinate[0] + intercept
            if y != coordinate[1]:
                return False
    return True
