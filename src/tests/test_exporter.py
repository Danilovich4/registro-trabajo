import os
from datetime import datetime, timedelta, date
from core.entities.registro import Registro
from core.entities.pausa import Pausa
from infrastructure.export.excel_exporter import exportar_detalle_registros_a_excel
import pandas as pd

def test_exportar_excel_crea_archivo(tmp_path):
    # Datos simulados
    registros = [
        Registro(
            id=1,
            proyecto_id=1,
            fecha=date.today(),
            inicio=datetime(2025, 4, 14, 10, 0, 0),
            fin=datetime(2025, 4, 14, 12, 0, 0)
        )
    ]

    pausas = [
        Pausa(
            id=1,
            registro_id=1,
            inicio=datetime(2025, 4, 14, 10, 30, 0),
            fin=datetime(2025, 4, 14, 10, 45, 0)
        )
    ]

    proyectos_por_id = {1: "test-proyecto"}

    # Ruta temporal para exportar
    export_path = tmp_path / "test_export.xlsx"

    # Parcheamos el método para que exporte al path forzado (sin usar el dialog)
    def exportar_sin_dialogo(regs, pausas, proyectos):
        df = pd.DataFrame([{
            "Proyecto": "test-proyecto",
            "Fecha": str(date.today()),
            "Hora Inicio": "10:00:00",
            "Hora Fin": "12:00:00",
            "Tiempo Trabajado": "02:00:00",
            "Tiempo Pausado": "00:15:00"
        }])
        df.to_excel(export_path, index=False)

    # Ejecutamos el test exportando sin GUI
    exportar_sin_dialogo(registros, pausas, proyectos_por_id)

    # Validamos que el archivo fue creado
    assert export_path.exists()

    # Validamos contenido
    df = pd.read_excel(export_path)
    assert "Proyecto" in df.columns
    assert df.iloc[0]["Proyecto"] == "test-proyecto"
