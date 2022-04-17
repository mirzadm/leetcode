"""Problem 89: Generate a circular sequence Gray codes"""

from typing import List

###############################################################################
# A solution based on the observation that each bit change follows a certain
# pattern.
###############################################################################

def _powers_of_two(n: int) -> List[int]:
    """Return a list of powers of 2 from 0 to n"""
    if n < 0:
        raise ValueError("n must be >= 0")
    powers = [1]
    for i in range(1, n + 1):
        powers.append(2 * powers[-1])
    return powers


def gray_code_sequence_generator(n: int) -> List[int]:
    """Return a circular list of n-bit gray codes starting at 0."""
    if n < 1:
        raise ValueError("n must be >= 1")
    gray_code_sequence = []
    powers_of_two = _powers_of_two(n)
    gray_code = 0
    gray_code_sequence.append(0)
    for i in range(1, powers_of_two[n]):
        for j in range(n):
            # The condition determines when to invert a certain bit
            # For instance, bit 1 changes every 4 bits starting at code number 2
            if i % powers_of_two[j + 1] == powers_of_two[j]:
                gray_code ^= powers_of_two[j]
                break # Only one bit changes in each iteration
        gray_code_sequence.append(gray_code)
    return gray_code_sequence

###############################################################################
# A solution using the simple mathematical formula of n ^ (n >> 1)
###############################################################################

def gray_code_formula(n: int) -> List[int]:
    if n < 1:
        raise ValueError("n must be >= 1")
    gray_codes = []
    for i in range(2 ** n):
        gray_codes.append(i ^ (i >> 1))
    return gray_codes
