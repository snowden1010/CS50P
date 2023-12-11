from twttr import shorten
import pytest


# using parameterize  from pytest 
@pytest.mark.parametrize(
    ("word, expected"),
    [
        ("AbdO", "bd"),
        ("ALi", "L"),
        ("aeiou", ""),
        ("AEIOU", ""),
        ("Twitter", "Twttr"),
        ("0123456789", "0123456789")
        

    ]
)

# testing 6 + 1 cases 
def test_shorten(word, expected):
    assert shorten(word) == expected
    assert shorten(",.") == ",."
    