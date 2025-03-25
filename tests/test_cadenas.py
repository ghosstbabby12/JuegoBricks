from src.cadenas import convertir_mayusculas

def test_convertir_mayusculas():
    assert convertir_mayusculas("python") == "PYTHON"
    assert convertir_mayusculas("Prueba") == "PRUEBA"
    assert convertir_mayusculas("123") == "123"
    assert convertir_mayusculas("") == ""