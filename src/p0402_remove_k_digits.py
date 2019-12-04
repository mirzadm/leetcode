"""Problem 402. Remove K Digits."""


##############################################################################
# O(n) solution
##############################################################################

def remove_k_digits(num: str, num_of_digits: int) -> str:
    """Removes digits from `num` resulting in smallest number.

    Time complexity: O(n).

    Args:
        `num`: String-formatted non-negative number with no leading zeros.
        `num_of_digits`: Number of digits to remove.
    Returns:
        String-formatted number after removing digits.
    Raises:
        IndexError: Invalid number of digits to remove.
    """
    if num_of_digits > len(num) or num_of_digits < 0:
        raise IndexError("Invalid number of digits to remove.")
    if num_of_digits == len(num):
        return "0"
    i = 0
    removed_digits = 0
    while removed_digits < num_of_digits:
        if i < len(num) - 1:
            if int(num[i]) > int(num[i + 1]):
                num = num[: i] + num[i + 1: ] # Drop i-th digit
                removed_digits += 1
                if i > 0:
                    i -= 1 # Backtrack to compare i-1 and i in next loop
            else:
                i += 1
        else: # Remove remaining digits from left end.
            num = num[: len(num) - (num_of_digits - removed_digits)]
            removed_digits = num_of_digits
    return str(int(num)) # Remove leading zeros


##############################################################################
# O(n^2) solution
##############################################################################

def remove_k_digits_n2(num: str, num_of_digits: int) -> str:
    """Removes digits from `num` resulting in smallest number.

    Time complexity: O(n^2)

    Args:
        `num`: String-formatted non-negative number with no leading zeros.
        `num_of_digits`: Number of digits to remove.
    Returns:
        String-formatted number after removing digits.
    Raises:
        IndexError: Invalid number of digits to remove.
    """
    if num_of_digits > len(num) or num_of_digits < 0:
        raise IndexError("Invalid number of digits to remove.")
    if num_of_digits == len(num):
        return "0"
    for i in range(num_of_digits):
        num = remove_one_digit(num)
    return str(int(num)) # Remove leading zeros


def remove_one_digit(num: str) -> str:
    """Removes one digit from `num` resulting in smallest number."""
    flag = False
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            flag = True
            break
    if flag:
        return num[:i] + num[i + 1:]
    else:
        return num[:len(num) - 1]
