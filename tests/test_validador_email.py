import pytest
from src.validador_email import validar_email

@pytest.mark.parametrize("email, esperado", [
    ("usuario@example.com", "Correo electrónico válido"),
    ("usuario@ejemplo", "Correo electrónico no válido"),  # Falta el dominio
    ("usuario@.com", "Correo electrónico no válido"),  # Dominio inválido
    ("usuario@ejemplo..com", "Correo electrónico no válido"),  # Doble punto
    ("usuario ejemplo@gmail.com", "El correo no debe contener espacios"),  # Contiene espacio
    ("usuario@ejemplo.com.co", "Correo electrónico válido"),  # Dominio con subdominio válido
])
def test_validar_email(email, esperado):
    assert validar_email(email) == esperado
