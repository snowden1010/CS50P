from bank import value


# testing hello, in upper and lower case
def test_value():
    assert value("hello Kramer") == 0
    assert value("HELLO KRAMER") == 0


# testing hey in both upper and lowr case
def test_value_hey():
    assert value("hey kramer") == 20
    assert value("HEY KRAMER") == 20


# testing other expressions
def test_value_other():
    assert value("wessup Kramer?") == 100
    assert value("WESSUP KRAMER?") == 100






