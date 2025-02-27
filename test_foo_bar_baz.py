import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here
def test_foo_bar_baz():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(17) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17"


def test_foo_bar_baz_negative():
    assert foo_bar_baz(-2) == ""
    assert foo_bar_baz(-3) == ""

def test_foo_bar_baz_non_int():
    try:
        assert foo_bar_baz(114.514) == ""
    except TypeError:
        pass

    try:
            assert foo_bar_baz("some random string") == ""
    except TypeError:
        pass