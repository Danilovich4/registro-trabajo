import sqlite3
from datetime import datetime
from core.entities.registro import Registro
from infrastructure.db.connection import get_connection

def crear_tabla_registros():
    """
    Crea la tabla 'registros' si no existe en la base de datos.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proyecto_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            inicio TEXT NOT NULL,
            fin TEXT,
            tiempo_total TEXT,
            pausas_total TEXT
        )
    """)

    conn.commit()
    conn.close()

def guardar_registro(registro: Registro):
    """
    Guarda un objeto Registro en la base de datos.
    :param registro: Instancia de Registro ya finalizada o en curso.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO registros (proyecto_id, fecha, inicio, fin, tiempo_total, pausas_total)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        registro.proyecto_id,
        str(registro.fecha),
        registro.inicio.isoformat(),
        registro.fin.isoformat() if registro.fin else None,
        str(registro.duracion_total()) if registro.fin else None,
        None  # Se calculará más adelante con la suma de pausas reales
    ))

    registro.id = cursor.lastrowid

    conn.commit()
    conn.close()
