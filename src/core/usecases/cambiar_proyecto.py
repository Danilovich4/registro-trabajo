from datetime import datetime
from core.entities.registro import Registro
from core.usecases.calcular_pausas_de_registro import calcular_pausas_de_registro

def cambiar_proyecto(registro_actual: Registro, nuevo_proyecto_id: int) -> tuple[Registro, Registro]:
    """
    Caso de uso: Cambiar de proyecto activo durante una jornada.

    Finaliza el registro actual y crea uno nuevo con el nuevo proyecto.

    :param registro_actual: Objeto Registro en curso.
    :param nuevo_proyecto_id: ID del nuevo proyecto seleccionado.
    :return: Tupla con (registro_finalizado, nuevo_registro)
    """
    if registro_actual.proyecto_id == nuevo_proyecto_id:
        raise ValueError("No puedes cambiar al mismo proyecto. Debe ser uno distinto al actual.")

    # Finalizar el bloque de trabajo actual
    registro_actual.finalizar()

    # Calcular y asignar total de pausas asociadas
    total_pausas = calcular_pausas_de_registro(registro_actual.id)
    registro_actual.pausas_total = total_pausas

    # Iniciar un nuevo bloque para el nuevo proyecto
    nuevo_registro = Registro(proyecto_id=nuevo_proyecto_id, inicio=datetime.now())

    return registro_actual, nuevo_registro
