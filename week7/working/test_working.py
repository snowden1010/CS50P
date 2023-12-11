import pytest
from working import convert


# using pytest's mark.parametrize decorator
@pytest.mark.parametrize(
    ("value", "expected"), [
        ("9 AM to 5 PM", "09:00 to 17:00"),
        ("12 PM to 6 AM", "12:00 to 06:00")
    ]
)
# def test_convert and passing in the value and expected return
def test_convert(value, expected):
    # asserting
    assert convert(value) == expected


@pytest.mark.parametrize(
    ("value",), [
        ("13 AM to 20 PM",),
        ("9 am to 5 pm",),
        ("9 AM - 5 PM",)
    ]
)
# def the function for handling exceptions
def test_convert_exception(value):
    with pytest.raises(ValueError):
        convert(value)
