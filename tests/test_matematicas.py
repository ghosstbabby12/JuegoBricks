import pytest
from src.matematicas import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-3)