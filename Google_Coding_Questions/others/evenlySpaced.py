"""
Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the three values are
evenly spaced, so the difference between small and medium is the same as the difference between medium and large.

evenlySpaced(2, 4, 6) → true
evenlySpaced(4, 6, 2) → true
evenlySpaced(4, 6, 3) → false
"""


def evenlySpaced(a, b, c):
    lst = sorted([a, b, c])
    if lst[1] - lst[0] == lst[2] - lst[1]:
        return True
    return False


def test_evenlySpaced():
    assert evenlySpaced(2, 4, 6) is True
    assert evenlySpaced(4, 6, 2) is True
    assert evenlySpaced(4, 6, 3) is False
    assert evenlySpaced(6, 2, 4) is True
    assert evenlySpaced(1, 3, 5) is True
    assert evenlySpaced(1, 3, 6) is False
    assert evenlySpaced(2, 4, 8) is False
    assert evenlySpaced(3, 6, 9) is True
    assert evenlySpaced(1, 1, 3) is False
    assert evenlySpaced(3, 3, 3) is True


test_evenlySpaced()
