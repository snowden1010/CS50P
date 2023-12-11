import pytest
from um import count


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("yummy", 0),
        ("um ", 1),
        (" um ", 1),
        ("Um, ", 1)
    ]
)
def test_convert(value, expected):
    assert count(value) == expected
