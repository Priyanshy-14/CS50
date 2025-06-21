from working import convert
import pytest

def test_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:05 PM to 9:15 PM") == "13:05 to 21:15"

def test_short_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"

def test_mixed_formats():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("9:00AM - 5:00PM")
    with pytest.raises(ValueError):
        convert("Lunch time is 12:00 PM to 1:00 PM")

