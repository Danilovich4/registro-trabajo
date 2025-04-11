from datetime import datetime
from core.entities.registro import Registro

def iniciar_registro(proyecto_id: int) -> Registro:
    """
    Caso de uso: Iniciar una jornada de trabajo sobre un proyecto.

    Crea un objeto Registro con la hora actual como inicio.

    :param proyecto_id: ID del proyecto seleccionado.
    :return: Objeto Registro listo para ser guardado o manipulado.
    """
    return Registro(proyecto_id=proyecto_id, inicio=datetime.now())
