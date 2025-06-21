
import pytest
from um import count

def test_count():
    assert count("um, my name is priyanshy!") == 1
    assert count("um,this is priyanshy! my um college is christ") == 2
    assert count("um,um, um ummm") == 3

def test_word():
    assert count("this is yummyyy") == 0
    assert count("An umbrella?") == 0
    assert count("um... um? Um! I said um. Not umm or yummy.") == 4

test_count()
test_word()
