"""Longest substring without repeating characters."""


def longest_non_repeating_substring(string: str) -> int:
    if not string:
        return 0
    left = 0
    right = 1
    max_len = 1
    while right < len(string):
        while string[right] in string[left: right]:
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


if __name__ == "__main__":
    print(longest_non_repeating_substring("a"))
    print(longest_non_repeating_substring("aa"))
    print(longest_non_repeating_substring("aaa"))
    print(longest_non_repeating_substring("abc"))
    print(longest_non_repeating_substring("abcdadef"))
