"""Problem 688: Knight Probability in Chessboard

k moves
probability of staying on the chess board
brute force: calculate all 8^k move combinations, find the ratio of staying on the board
(row, col)

1
2
3
...
k

Here is the idea:

n*n cell each can have their probability of staying on the board.
p1 = Start at (row, col) = 1/8 * probably(each next cell on the board)
p2 = p1 *

p(k) = 1/8 * sum(p(k-1) for all neighboring nodes)
We need to store neighboring nodes p(i) for i in [1, k] for each node
The upper bound for number of calls is k*n^2
"""

from typing import List, Dict, Tuple


def knight_probability(n: int, k: int, row: int, column: int) -> float:
    if k == 0:
        return 1.0
    probability_matrix = [[{} for _ in range(n)] for _ in range(n)]
    return _knight_probability(n, k, row, column, probability_matrix)


def _knight_probability(
    n: int,
    k: int,
    row: int,
    column: int,
    probability_matrix: List[List[Dict[int, float]]],
) -> float:
    if k not in probability_matrix[row][column]:
        probability = 0.0
        for neighbor in _neighbors(n, row, column):
            if k == 1:
                probability += 0.125
            else:
                probability += 0.125 * _knight_probability(
                    n, k - 1, neighbor[0], neighbor[1], probability_matrix
                )
        probability_matrix[row][column][k] = probability
    return probability_matrix[row][column][k]


def _neighbors(n: int, row: int, column: int) -> List[Tuple[int, int]]:
    offsets = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
    neighbors = []
    for row_offset, col_offset in offsets:
        neighbor = (row + row_offset, column + col_offset)
        if (0 <= neighbor[0] < n) and (0 <= neighbor[1] < n):
            neighbors.append(neighbor)
    return neighbors
