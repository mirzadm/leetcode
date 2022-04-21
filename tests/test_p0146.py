import pytest
from src.p0146_lru_cache import LRUCache


def test_lru_cache():
    with pytest.raises(RuntimeError):
        lru = LRUCache(0)
    lru = LRUCache(1)
    assert lru.get(10) == -1
    lru.put(10, "A")
    assert lru.get(10) == "A"
    lru.put(20, "B")
    assert lru.get(20) == "B"
    assert lru.get(10) == -1
