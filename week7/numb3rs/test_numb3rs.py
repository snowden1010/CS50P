from numb3rs import validate
import pytest

@pytest.mark.parametrize(
    ("ip", "validation"),
    [
        ("275.3.6.28", False),
        ("1.999.1.1", False),
        ("foo", False),
        ("1.1.1.1.1", False)
    ]
)


def test_validate(ip, validation):
    assert validate(ip) == validation