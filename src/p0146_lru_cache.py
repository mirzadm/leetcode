"""LRU cache."""

class Node:
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
        self.map = dict()

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._make_most_recent(node)
        return node.value

    def put(self, key, value):
        if key not in self.map:
            if self.length == self.size:
                self._evict_least_recent()
            self._add_most_recent(key, value)
        else:
            node = self.map[key]
            node.value = value
            self._make_most_recent(node)

    def _make_most_recent(self, node):
        if node == self.head:
            return
        if node == self.tail:
            right_node = node.right
            self.tail = right_node
            right_node.left = None
        else:
            left_node = node.left
            right_node = node.right
            left_node.right = right_node
            right_node.left = left_node
        node.right = None
        node.left = self.head
        self.head.right = node
        self.head = node

    def _evict_least_recent(self):
        node = self.tail
        self.map.pop(node.key)
        self.tail = node.right
        if self.tail is None:
            self.head = None
        self.length -= 1

    def _add_most_recent(self, key, value):
        node = Node(key, value)
        self.map[key] = node
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.right = node
            node.left = self.head
            self.head = node
        self.length += 1


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(2, 1)
    c.put(2, 2)
    print(c.get(1))
    c.put(3, 30)
    print(c.get(2))
    c.put(4, 40)
    print(c.get(1))
    print(c.get(2))
    print(c.get(3))
    print(c.get(4))
