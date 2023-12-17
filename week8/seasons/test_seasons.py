import pytest
from seasons import minutes, word_it
from datetime import datetime, date


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2023-12-16", 0),
        ("2022-12-16", 525_600),
        ("2021-12-16", 1_051_200),
        ("1990-12-16", 17_356_320)

    ]
)
def test_minutes(value, expected):
    today = "2023-12-16"
    today = datetime.strptime(today, "%Y-%m-%d").date()
    assert minutes(value, today) == expected


def test_invalid_date(capsys):
    with pytest.raises(ValueError):
        minutes("2022-22-22", date.today())
        minutes("January 1, 1999 ", date.today())


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
