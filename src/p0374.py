"""Problem 374. Guess Number Higher or Lower

Guess the SCERET number.
"""


def guess_number(n: int) -> int:
    return _guess_number(left=1, right=n)


def _guess_number(left: int, right: int) -> int:
    mid = (left + right) // 2
    if guess(mid) == -1:
        return _guess_number(left, mid - 1)
    elif guess(mid) == 1:
        return _guess_number(mid + 1, right)
    else:
        return mid


# The helper function to give hints.
def guess(num: int) -> int:
    pick = 7
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0
