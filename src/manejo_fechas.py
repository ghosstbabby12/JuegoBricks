from datetime import datetime

def calcular_dias_entre_fechas(fecha1: str, fecha2: str) -> int:
    """
    Calcula la cantidad de días entre dos fechas en formato 'YYYY-MM-DD'.

    :param fecha1: Primera fecha en formato 'YYYY-MM-DD'.
    :param fecha2: Segunda fecha en formato 'YYYY-MM-DD'.
    :return: Número de días entre ambas fechas.
    """
    try:
        f1 = datetime.strptime(fecha1, "%Y-%m-%d")
        f2 = datetime.strptime(fecha2, "%Y-%m-%d")
        return abs((f2 - f1).days)
    except ValueError:
        raise ValueError("Formato de fecha incorrecto. Use 'YYYY-MM-DD'.")
