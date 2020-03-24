"""Minimum hours till no fresh oranges are left.

0: empty cell
1: fresh orange
2: rotten orange
"""

from collections import deque


def rotting_oranges(grid):
    queue = deque()
    hour = 0
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 2:
                queue.append((r, c, hour))
    while queue:
        r, c, hour = queue.popleft()
        for nr, nc in neighbors(r, c, grid):
            if grid[nr][nc] == 1:
                queue.append((nr, nc, hour + 1))
                grid[nr][nc] = 2
    if fresh_oranges(grid):
        return -1
    else:
        return hour


def neighbors(row, col, grid):
    potential_neighbors = (
        (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
    )
    for nr, nc in potential_neighbors:
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            yield nr, nc


def fresh_oranges(grid):
    return any(1 in row for row in grid)
