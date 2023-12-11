import pytest
from seasons import minutes, word_it


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2023-11-16", 0),
        ("1999-12-31", 12558240),
        ("2022-11-16", 525600)
    ]
)
def test_minutes(value, expected):
    assert minutes(value) == expected


def test_invalid_date(capsys):
    with pytest.raises(ValueError):
        minutes("2022-22-22")
        minutes("January 1, 1999 ")





@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (1, "One minutes"),
        (12220, "Twelve thousand, two hundred twenty minutes"),
        (122, "One hundred twenty-two minutes")
    ]
)
def test_word_it(value, expected):
    assert word_it(value) == expected
    assert word_it(minutes("2020-12-17")) == "One million, five hundred thirty-two thousand, one hundred sixty minutes"
