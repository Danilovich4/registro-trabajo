from datetime import datetime
from core.entities.pausa import Pausa

def registrar_pausa(registro_id: int, inicio: datetime, fin: datetime) -> Pausa:
    """
    Caso de uso: Registrar una pausa por inactividad.

    :param registro_id: ID del registro al que se asocia la pausa.
    :param inicio: Hora en la que comenzó la inactividad.
    :param fin: Hora en la que terminó la inactividad.
    :return: Objeto Pausa creado y listo para ser guardado.
    """
    return Pausa(registro_id=registro_id, inicio=inicio, fin=fin)
