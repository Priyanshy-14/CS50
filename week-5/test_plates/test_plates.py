import pytest
from plates import is_valid

def test_len():
    assert is_valid("ab123") == True
    assert is_valid("abcd234") == False

def test_alphabet():
    assert is_valid("abcde2") == True
    assert is_valid("89cd10") == False

def test_num():
    assert is_valid("ab999") == True
    assert is_valid("xxx023") == False

def test_punctuation():
    assert is_valid("ab,999") == False
