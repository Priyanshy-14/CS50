import pytest
from numb3rs import validate

def test_true_case():
    assert validate("2.2.2.2") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_false_case():
    assert validate("2.2.2.") == False
    assert validate("0.0.0...") == False
    assert validate("255.255.255.255.") == False
    assert validate("64.128.256.512") == False

test_true_case()
test_false_case()

