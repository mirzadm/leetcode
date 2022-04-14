"""Problem 89: Generate a circular sequence Gray codes"""

from typing import List


def _convert_to_int(bits: List[int]) -> int:
    """Convert a list of 0/1 to unsigned int, left being less significant"""
    if bits == []:
        raise ValueError("bits must not be empty")
    power = 1
    num = 0
    for b in bits:
        num += b * power
        power <<= 1
    return num


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
    gray_code_nums = []
    powers_of_two = _powers_of_two(n)
    gray_code = [0] * n
    gray_code_nums.append(0)
    for i in range(1, powers_of_two[n]):
        for j in range(n):
            # The following condition determines when to switch a certain bit
            if i % powers_of_two[j + 1] == powers_of_two[j]:
                gray_code[j] = 1 - gray_code[j]
        gray_code_nums.append(_convert_to_int(gray_code))
    return gray_code_nums


if __name__ == "__main__":
    print(gray_code_sequence_generator(4))
