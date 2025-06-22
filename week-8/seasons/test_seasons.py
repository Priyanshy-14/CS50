import pytest
from datetime import date
from seasons import calculate_minutes, convert_to_words


def test_calculate_minutes():
    assert calculate_minutes(date(2022, 1, 1), date(2023, 1, 1)) == 525600
    assert calculate_minutes(date(2020, 1, 1), date(2021, 1, 1)) == 527040

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(527040) == "Five hundred twenty-seven thousand forty"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred"
