def obtener_maximo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return max(lista)

def obtener_minimo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return min(lista)

def calcular_promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista) / len(lista)
