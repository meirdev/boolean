import pytest

from boolean import boolean, is_false, is_true


@pytest.mark.parametrize(
    "value, expected",
    [
        (False, False),
        (True, True),
        (1, True),
        (0, False),
        ("y", True),
        ("yes", True),
        ("t", True),
        ("true", True),
        ("on", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("f", False),
        ("false", False),
        ("off", False),
        ("0", False),
    ],
)
def test_boolean(value, expected):
    assert boolean(value) == expected


def test_invalid_value():
    for i in ["hello", 100, 1.0, None]:
        with pytest.raises(ValueError):
            boolean(i)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("f", True),
        ("t", False),
    ],
)
def test_is_false(value, expected):
    assert is_false(value) is expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0", False),
        ("1", True),
    ],
)
def test_is_true(value, expected):
    assert is_true(value) is expected
