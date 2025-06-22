from jar import Jar
import pytest

def test_capacity_and_size():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

def test_deposit():
    jar = Jar(3)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
