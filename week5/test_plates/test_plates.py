from plates import is_valid
import pytest


# using pytest to automate the value and the expected return
# including the corner cases as values to is_valid()
@pytest.mark.parametrize(
        ("value, expected"),
        [
            ("CS50", True),
            ("AAAA2222", False),
            ("A5", False),
            ("AAA22A", False),
            ("CS05", False),
            ("AA22!", False),
            
            
        ]
)


# defining the test function.
def test_is_valid(value, expected):
    assert is_valid(value) == expected