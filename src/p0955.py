"""Problem 955. Delete Columns to Make Sorted II

Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from typing import List


def min_deletion_size(words: List[str]) -> int:
    current_index = 0
    deleted_chars = 0
    while current_index < len(words[0]):
        any_equal_to = False
        any_greater_than = False
        for i in range(len(words) - 1):
            if words[i][:current_index + 1] > words[i + 1][:current_index + 1]:
                any_greater_than = True
                break
        if any_greater_than:
            deleted_chars += 1
            words = _delete_char(words, current_index)
        else:
            for i in range(len(words) - 1):
                if words[i][:current_index + 1] == words[i + 1][:current_index + 1]:
                    any_equal_to = True
                    break
            if any_equal_to:
                current_index += 1
            else:
                return deleted_chars

    return deleted_chars


def _delete_char(words: List[str], index_to_delete: int) -> List[str]:
    return [word[: index_to_delete] + word[index_to_delete + 1:] for word in words]
