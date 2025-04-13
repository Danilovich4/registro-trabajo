from datetime import date
from core.entities.registro import Registro
from core.entities.pausa import Pausa

def consultar_registros_por_fecha(
    fecha: date,
    registros: list[Registro],
    pausas: list[Pausa]
) -> dict:
    """
    Caso de uso: Consultar todos los registros y pausas de una fecha concreta.

    :param fecha: Fecha deseada (ej. date(2025, 4, 10))
    :param registros: Lista completa de registros cargados externamente.
    :param pausas: Lista completa de pausas cargadas externamente.
    :return: Diccionario con listas filtradas por fecha.
    """
    registros_dia = [r for r in registros if r.fecha == fecha]
    pausas_dia = [p for p in pausas if p.inicio.date() == fecha]

    return {
        "fecha": fecha,
        "registros": registros_dia,
        "pausas": pausas_dia
    }
