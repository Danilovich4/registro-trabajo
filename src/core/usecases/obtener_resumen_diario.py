from datetime import date, timedelta
from core.entities.registro import Registro
from core.entities.pausa import Pausa

def obtener_resumen_diario(
    fecha: date,
    registros: list[Registro],
    pausas: list[Pausa],
    proyectos_por_id: dict[int, str]
) -> dict:
    """
    Genera un resumen de trabajo por día y por proyecto.

    :param fecha: Fecha del resumen a calcular.
    :param registros: Lista de objetos Registro en esa jornada.
    :param pausas: Lista de objetos Pausa ocurridas en esa jornada.
    :param proyectos_por_id: Diccionario que relaciona ID con nombre del proyecto.
    :return: Diccionario con resumen diario completo.
    """
    resumen = {
        "fecha": str(fecha),
        "proyectos": {},
        "total_trabajado": timedelta(),
        "total_pausas": timedelta()
    }

    # Filtrar registros del día
    registros_dia = [r for r in registros if r.fecha == fecha]

    for r in registros_dia:
        nombre_proyecto = proyectos_por_id.get(r.proyecto_id, f"Proyecto {r.proyecto_id}")
        duracion = r.duracion_total()

        if nombre_proyecto not in resumen["proyectos"]:
            resumen["proyectos"][nombre_proyecto] = {
                "tiempo_trabajado": timedelta(),
                "pausas": timedelta()
            }

        resumen["proyectos"][nombre_proyecto]["tiempo_trabajado"] += duracion
        resumen["total_trabajado"] += duracion

    # Filtrar pausas del día
    pausas_dia = [p for p in pausas if p.inicio.date() == fecha]

    for p in pausas_dia:
        duracion_pausa = p.duracion()
        resumen["total_pausas"] += duracion_pausa

    return resumen
