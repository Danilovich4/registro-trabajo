from core.entities.registro import Registro
from datetime import datetime, timedelta
from core.usecases.calcular_pausas_de_registro import calcular_pausas_de_registro  

def finalizar_jornada(registro_actual: Registro) -> Registro:
    """
    Caso de uso: Finalizar la jornada actual.

    Marca la hora de finalización del registro actual si aún está abierto.

    :param registro_actual: Objeto Registro en curso.
    :return: El mismo objeto Registro con el campo 'fin' actualizado.
    """
    if registro_actual.fin is not None:
        raise ValueError("La jornada ya ha sido finalizada.")

    registro_actual.finalizar()
    total_pausas = calcular_pausas_de_registro(registro_actual.id)
    registro_actual.pausas_total = total_pausas
    
    return registro_actual
