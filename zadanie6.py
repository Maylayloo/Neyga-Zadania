import pytest


def romanToInt(s: str) -> int:
    # Your code goes here
    pass


@pytest.mark.parametrize("roman_input,expected_integer", [
    ("III", 3),
    ("XV", 15),
    ("VI", 6),
    ("IV", 4),
    ("XC", 90),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_romanToInt(roman_input, expected_integer):
    assert romanToInt(roman_input) == expected_integer


def test_romanToInt_InvalidInput():
    with pytest.raises(ValueError, match="Nie ma takiej liczby w systemie Rzymskim!"):
        romanToInt("ABCDEM")
