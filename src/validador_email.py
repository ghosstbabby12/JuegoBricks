import re

def validar_email(email: str) -> str:
    """
    Valida si un correo electrónico es válido.
    
    - Debe contener "@" y un dominio válido.
    - No debe contener espacios.
    - No debe tener puntos consecutivos en el dominio.
    - El dominio debe incluir una extensión como ".com" o ".org".
    """
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$"
    
    if " " in email:
        return "El correo no debe contener espacios"
    
    if ".." in email.split("@")[-1]:  # Verifica si hay dos puntos seguidos en el dominio
        return "Correo electrónico no válido"
    
    if not re.match(patron, email):
        return "Correo electrónico no válido"
    
    return "Correo electrónico válido"
