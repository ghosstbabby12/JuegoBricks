import re

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    if not re.search(r"[A-Z]", contraseña):
        return "La contraseña debe contener al menos una letra mayúscula"
    if not re.search(r"\d", contraseña):
        return "La contraseña debe contener al menos un número"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        return "La contraseña debe contener al menos un carácter especial"
    return "Contraseña válida"
