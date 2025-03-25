def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]