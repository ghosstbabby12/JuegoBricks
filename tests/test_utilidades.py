import pytest 
from src.utilidades import es_par # Importa el módulo desde el paquete src 
def test_placeholder(): 
    assert True  # TODO: Reemplazar con pruebas reales


def test_es_par():
    assert es_par(2) is True
    assert es_par(3) is False
    assert es_par(0) is True
    assert es_par(-4) is True
    assert es_par(-5) is False