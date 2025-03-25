import pytest
from src.operaciones_lista import obtener_maximo, obtener_minimo, calcular_promedio

def test_obtener_maximo():
    assert obtener_maximo([1, 2, 3, 4, 5]) == 5
    assert obtener_maximo([-10, -5, 0, 5, 10]) == 10
    with pytest.raises(ValueError):
        obtener_maximo([])

def test_obtener_minimo():
    assert obtener_minimo([1, 2, 3, 4, 5]) == 1
    assert obtener_minimo([-10, -5, 0, 5, 10]) == -10
    with pytest.raises(ValueError):
        obtener_minimo([])

def test_calcular_promedio():
    assert calcular_promedio([10, 20, 30]) == 20
    assert calcular_promedio([5, 10, 15, 20]) == 12.5
    with pytest.raises(ValueError):
        calcular_promedio([])
