import pandas as pd
from datetime import timedelta, date
from pathlib import Path
from tkinter import filedialog
from tkinter import Tk
from core.entities.registro import Registro
from core.entities.pausa import Pausa

def exportar_detalle_registros_a_excel(
    registros: list[Registro],
    pausas: list[Pausa],
    proyectos_por_id: dict[int, str]
):
    """
    Exporta un informe detallado con una fila por registro, incluyendo proyecto, fecha, inicio, fin,
    tiempo trabajado y pausas asociadas.
    """
    pausas_por_registro = {}
    for pausa in pausas:
        if pausa.registro_id not in pausas_por_registro:
            pausas_por_registro[pausa.registro_id] = []
        pausas_por_registro[pausa.registro_id].append(pausa)

    data = []

    for reg in registros:
        if not reg.fin:
            continue

        duracion = reg.duracion_total()

        pausas = pausas_por_registro.get(reg.id, [])
        total_pausa = timedelta()
        for pausa in pausas:
            if pausa.fin:
                total_pausa += pausa.fin - pausa.inicio

        data.append({
            "Proyecto": proyectos_por_id.get(reg.proyecto_id, "Desconocido"),
            "Fecha": str(reg.fecha),
            "Hora Inicio": reg.inicio.strftime("%H:%M:%S"),
            "Hora Fin": reg.fin.strftime("%H:%M:%S"),
            "Tiempo Trabajado": _formatear_tiempo(duracion),
            "Tiempo Pausado": _formatear_tiempo(total_pausa),
        })

    if not data:
        print("⚠️ No hay registros para exportar.")
        return

    df = pd.DataFrame(data)

    # 👉 Preguntar dónde guardar el archivo
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    nombre_archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Archivos Excel", "*.xlsx")],
        initialfile=f"detalle_registros_{date.today().isoformat()}",
        title="Guardar resumen como..."
    )

    if not nombre_archivo:
        print("❌ Exportación cancelada.")
        return

    df.to_excel(Path(nombre_archivo), index=False)
    print(f"✅ Informe detallado exportado: {nombre_archivo}")

def _formatear_tiempo(td: timedelta) -> str:
    total_segundos = int(td.total_seconds())
    horas, resto = divmod(total_segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:02}:{minutos:02}:{segundos:02}"
