import pytest
from src.manejo_fechas import calcular_dias_entre_fechas

def test_calculo_correcto():
    assert calcular_dias_entre_fechas("2024-03-01", "2024-03-10") == 9
    assert calcular_dias_entre_fechas("2024-01-01", "2024-01-31") == 30

def test_mismo_dia():
    assert calcular_dias_entre_fechas("2024-05-10", "2024-05-10") == 0

def test_formato_incorrecto():
    with pytest.raises(ValueError):
        calcular_dias_entre_fechas("10-05-2024", "2024-05-10")

def test_fecha_invertida():
    assert calcular_dias_entre_fechas("2024-05-10", "2024-05-01") == 9
