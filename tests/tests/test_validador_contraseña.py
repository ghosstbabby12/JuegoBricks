import pytest
from src.validador_contraseña import validar_contraseña

@pytest.mark.parametrize("contraseña, esperado", [
    ("Abc123!", "Contraseña válida"),
    ("abcdefg", "La contraseña debe tener al menos 8 caracteres"),
    ("ABCDEFG123", "La contraseña debe contener al menos un carácter especial"),
    ("abcdefg!", "La contraseña debe contener al menos una letra mayúscula"),
    ("ABCdefg!", "La contraseña debe contener al menos un número"),
])
def test_validar_contraseña(contraseña, esperado):
    assert validar_contraseña(contraseña) == esperado
