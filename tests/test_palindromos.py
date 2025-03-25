from src.palindromos import es_palindromo

def test_es_palindromo():
    assert es_palindromo("radar") is True
    assert es_palindromo("oso") is True
    assert es_palindromo("python") is False
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("12321") is True
    assert es_palindromo("12345") is False