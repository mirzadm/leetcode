"""Can the frog cross the river?"""

from collections import defaultdict
from typing import Dict, List, Set


def can_cross(stones: List[int]) -> bool:
    if not stones:
        return False
    tried_combinations = defaultdict(set)
    return _can_cross(stones, 0, 0, tried_combinations)


def _can_cross(
    stones: List[int],
    position: int,
    last_jump: int,
    tried_combinations: Dict[int, Set[int]]
) -> bool:
    if position == len(stones) - 1:
        return True
    next_jumps = (i for i in (last_jump - 1, last_jump, last_jump + 1) if i > 0)
    for jump in next_jumps:
        if jump not in tried_combinations[position]:
            next_value = stones[position] + jump
            next_position = _find_index(stones, position + 1, next_value)
            if next_position != -1:
                if _can_cross(stones, next_position, jump, tried_combinations):
                    return True
                else:
                    tried_combinations[position].add(jump)
    return False


def _find_index(stones: List[int], start: int, value: int) -> int:
    try:
        index = stones.index(value, start)
        return index
    except ValueError:
        return -1


if __name__ == "__main__":
    print(can_cross([0,1,3,5,6,8,12,17]))
    print(can_cross([0,1,2,3,4,8,9,11]))
