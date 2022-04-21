"""LRU cache.

Implement least-recently-used (LRU) cache as a doubly linked list.
"""

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, size):
        if size <= 0:
            raise RuntimeError(f"Invalid cache size {size}. Size must be > 0.")
        self.size = size
        self.head = None
        self.tail = None
        self.length = 0
        self.key_value_store = dict()

    def get(self, key):
        if key not in self.key_value_store:
            return -1
        item = self.key_value_store[key]
        self._set_most_recent(item)
        return item.value

    def put(self, key, value):
        if key not in self.key_value_store:
            self._add_new_item(key, value)
        else:
            item = self.key_value_store[key]
            item.value = value
            self._set_most_recent(item)

    def _set_most_recent(self, item):
        if item == self.head:
            return
        if item == self.tail:
            right_item = item.right
            self.tail = right_item
            right_item.left = None
        else:
            left_item = item.left
            right_item = item.right
            left_item.right = right_item
            right_item.left = left_item
        item.right = None
        item.left = self.head
        self.head.right = item
        self.head = item

    def _evict_least_recent(self):
        item = self.tail
        self.key_value_store.pop(item.key)
        self.tail = item.right
        if self.tail is None:
            self.head = None
        self.length -= 1

    def _add_new_item(self, key, value):
        if self.length == self.size:
            self._evict_least_recent()
        item = Item(key, value)
        self.key_value_store[key] = item
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.head.right = item
            item.left = self.head
            self.head = item
        self.length += 1
