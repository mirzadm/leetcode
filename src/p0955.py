"""Problem 955. Delete Columns to Make Sorted II

Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from typing import List


def min_deletion_size(words: List[str]) -> int:
    word_length = len(words[0])
    current_index = 0
    deleted_chars = 0
    while current_index < word_length:
        any_equal_to = False
        any_greater_than = False
        for i in range(len(words) - 1):
            if words[i][:current_index + 1] > words[i + 1][:current_index + 1]:
                # Delete this character
                deleted_chars += 1
                any_greater_than = True
                words = _delete_char(words, current_index)
                break
        if not any_greater_than:
            for i in range(len(words) - 1):
                if words[i][:current_index + 1] == words[i + 1][:current_index + 1]:
                    any_equal_to = True
                    break
            if not any_equal_to:
                return deleted_chars
        current_index += 1
    return deleted_chars


def _delete_char(words: List[str], index_to_delete: int) -> List[str]:
    return [word[: index_to_delete] + word[index_to_delete + 1:] for word in words]
