"""Problme 402. Remove K Digits."""


def remove_k_digits(num: str, k: int) -> str:
    if k > len(num):
        raise IndexError("Invalid number of digits `k`.")
    if k == len(num):
        return 0
    for i in range(k):
        num = remove_one_digit(num)
    return num


def remove_one_digit(num: str) -> str:
    min_value = int(num)
    for i in range(len(num)):
        partial_value = int(num[:i] + num[i+1:])
        if partial_value < min_value:
            min_value = partial_value
    return str(min_value)


if __name__ == "__main__":
    print(remove_k_digits("435", 1))
    print(remove_k_digits("435", 2))
    print(remove_k_digits("435", 3))
