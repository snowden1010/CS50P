import pytest
from jar import Jar


def test_init():
   jar = Jar()
   assert jar.capacity == 12 


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


@pytest.mark.parametrize(
        ("value", "expected"),[
            (12, 12),
            (8, 8),
            (1, 1),
            (0, 0)
        ]
)
def test_deposit(value, expected):
    jar = Jar()
    jar.deposit(value)
    assert jar.size == expected


def test_deposit_exception():
    jar= Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit(14)
        jar.deposit(200)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7


def test_withdraw_exception():
    jar = Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(11)
        jar.withdraw(200)