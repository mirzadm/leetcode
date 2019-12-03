"""Problme 402. Remove K Digits.

Remove K digits so that the resulting number is the smallest possible.
"""

##############################################################################
# O(n) solution
##############################################################################

def remove_k_digits(num: str, digits_to_remove: int) -> str:
    if digits_to_remove > len(num) or digits_to_remove < 0:
        raise IndexError("Invalid number of digits to remove.")
    if digits_to_remove == len(num):
        return "0"
    i = 0
    k = 0
    while k < digits_to_remove:
        if i == len(num) - 1:
            num = num[: len(num) - (digits_to_remove - k)]
            k = digits_to_remove
        elif int(num[i]) > int(num[i + 1]):
            num = num[: i] + num[i + 1: ]
            k += 1
            if i > 0:
                i -= 1
        else:
            i += 1
    return str(int(num)) # Remove leading zeros


##############################################################################
# O(n^2) solution
##############################################################################

def remove_k_digits_n2(num: str, digits_to_remove: int) -> str:
    if digits_to_remove > len(num) or digits_to_remove < 0:
        raise IndexError("Invalid number of digits to remove.")
    if digits_to_remove == len(num):
        return "0"
    for i in range(digits_to_remove):
        num = remove_one_digit(num)
    return str(int(num)) # Remove leading zeros


def remove_one_digit(num: str) -> str:
    flag = False
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            flag = True
            break
    if flag:
        return num[:i] + num[i + 1:]
    else:
        return num[:len(num) - 1]
