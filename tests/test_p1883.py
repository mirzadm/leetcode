from src.p1883_min_skips import min_skips


def test_min_skips():
    # Impossible case
    assert min_skips(dist=[3], speed=2, hoursBefore=1) == -1
    assert min_skips(dist=[3, 2], speed=2, hoursBefore=2) == -1
    # Possible
    # No skips
    assert min_skips(dist=[3], speed=2, hoursBefore=2) == 0
    assert min_skips(dist=[3, 3], speed=2, hoursBefore=4) == 0
    # 1 skip
    assert min_skips(dist=[3, 3], speed=2, hoursBefore=3) == 1
    # 2 skips
    assert min_skips(dist=[3, 3, 2], speed=2, hoursBefore=4) == 2
