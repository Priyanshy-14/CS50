import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("1/2") == 50.0
    assert convert("3/4") == 75.0
    assert convert("1/100") == 1.0

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_error():
    with pytest.raises(ValueError):
        convert("3/2")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_format():
    with pytest.raises(ValueError):
        convert("abc")


