import pytest
from twttr import shorten

def test_i_and_e():
    assert shorten("twitter") == "twttr"
def test_a():
    assert shorten("apple") == "ppl"
def test_o():
    assert shorten("omega") == "mg"
def test_u():
    assert shorten("uncle") == "ncl"
def test_I_and_E():
    assert shorten("TWITTER") == "TWTTR"
def test_A():
    assert shorten("APPLE") == "PPL"
def test_O():
    assert shorten("OMEGA") == "MG"
def test_U():
    assert shorten("UNCLE") == "NCL"
def test_input():
    assert shorten("abc123") == "bc123"
def test_punctuation():
    assert shorten("Hello! How are you?") == "Hll! Hw r y?"

