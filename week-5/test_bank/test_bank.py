import pytest
from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hey") == 20

def test_greeting():
    assert value("what's up") == 100
