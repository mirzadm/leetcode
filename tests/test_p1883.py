from src.p1883_min_skips import min_skips


def test_min_skips():
    # Impossible case
    assert min_skips(dist=[3], speed=2, hours_before=1) == -1
    assert min_skips(dist=[3, 2], speed=2, hours_before=2) == -1
    # Possible
    # No skips
    assert min_skips(dist=[3], speed=2, hours_before=2) == 0
    assert min_skips(dist=[3, 3], speed=2, hours_before=4) == 0
    # 1 skip
    assert min_skips(dist=[3, 3], speed=2, hours_before=3) == 1
    # 1 skip
    assert min_skips(dist=[3, 3, 2], speed=2, hours_before=4) == 1
    # More complex example
    assert min_skips(dist=[.3, .2, .7, 0, .8, .1, .6], speed=1, hours_before=6) == 0
    assert min_skips(dist=[.3, .2, .7, 0, .8, .1, .6], speed=1, hours_before=5) == 1
    assert min_skips(dist=[.3, .2, .7, 0, .8, .1, .6], speed=1, hours_before=4) == 2
    assert min_skips(dist=[.3, .2, .7, 0, .8, .1, .6], speed=1, hours_before=3) == 5

