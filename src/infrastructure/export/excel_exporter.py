import pandas as pd
from pathlib import Path
from datetime import timedelta

def exportar_resumen_diario_a_excel(resumen: dict):
    """
    Exporta un resumen diario generado previamente a un archivo Excel.

    :param resumen: Diccionario generado por 'obtener_resumen_diario()'
    """
    fecha = resumen["fecha"]
    nombre_archivo = f"resumen_diario_{fecha}.xlsx"
    ruta_salida = Path(nombre_archivo)

    proyectos_data = []

    for nombre_proyecto, datos in resumen["proyectos"].items():
        proyectos_data.append({
            "Proyecto": nombre_proyecto,
            "Tiempo trabajado (HH:MM)": _formatear_tiempo(datos["tiempo_trabajado"]),
            "Pausas (HH:MM)": _formatear_tiempo(datos["pausas"])
        })

    df = pd.DataFrame(proyectos_data)

    # Añadimos totales como fila final
    total_row = {
        "Proyecto": "TOTAL",
        "Tiempo trabajado (HH:MM)": _formatear_tiempo(resumen["total_trabajado"]),
        "Pausas (HH:MM)": _formatear_tiempo(resumen["total_pausas"])
    }
    df.loc[len(df)] = total_row

    df.to_excel(ruta_salida, index=False)
    print(f"Resumen diario exportado a: {ruta_salida.absolute()}")

def _formatear_tiempo(td: timedelta) -> str:
    """
    Convierte un timedelta a un string HH:MM
    """
    total_minutos = int(td.total_seconds() // 60)
    horas, minutos = divmod(total_minutos, 60)
    return f"{horas:02}:{minutos:02}"
