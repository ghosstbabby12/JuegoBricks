import pytest
from src.gestor_usuarios import GestorUsuarios

@pytest.fixture
def gestor():
    return GestorUsuarios()

def test_agregar_usuario(gestor):
    gestor.agregar_usuario("usuario1")
    assert "usuario1" in gestor.usuarios

    with pytest.raises(ValueError):
        gestor.agregar_usuario("usuario1")  # Usuario ya existe

def test_eliminar_usuario(gestor):
    gestor.agregar_usuario("usuario2")
    gestor.eliminar_usuario("usuario2")
    assert "usuario2" not in gestor.usuarios

    with pytest.raises(ValueError):
        gestor.eliminar_usuario("usuario2")  # Usuario ya eliminado

def test_existe_usuario(gestor):
    gestor.agregar_usuario("usuario3")
    assert gestor.existe_usuario("usuario3") is True
    assert gestor.existe_usuario("usuario4") is False
