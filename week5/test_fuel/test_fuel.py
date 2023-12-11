from fuel import convert, gauge
import pytest


# checking anomelous cases
@pytest.mark.parametrize(
        ("value, expected"),
        [
            ("1/4", 25),
            ("0/2", 0),
        

        ]
)


# testing convert
def test_convert(value, expected):
    assert convert(value) == expected

# testing onvert's raising of ZeroDevisionErro
def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


# testing convert on ValueError exceptions, when x is > y    
def test_convert_other():
    with pytest.raises(ValueError):
        convert("3/2")
        

@pytest.mark.parametrize(
        ("percentage, result"),
        [
            (1, "E"),
            (0, "E"),
            (99, "F"),
            (100, "F"),
            (50, "50%")

        ]
)

# testing gauge on it's return

def test_gauge(percentage, result):
    assert gauge(percentage) == result