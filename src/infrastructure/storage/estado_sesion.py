import sqlite3
from pathlib import Path
from datetime import datetime, date
from core.entities.registro import Registro
from infrastructure.db.connection import get_connection

# Archivo de sesión persistente (usamos el mismo sistema SQLite)
SEGUIMIENTO_PATH = Path("timetrack.db")  # Ya usamos esta BD centralizada

def crear_tablas_sesion():
    """
    Crea las tablas necesarias para guardar estado de sesión.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sesion_activa (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            registro_id INTEGER NOT NULL,
            proyecto_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            inicio TEXT NOT NULL,
            en_pausa INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pausa_temporal (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            registro_id INTEGER NOT NULL,
            inicio TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def guardar_estado_sesion(registro: Registro, en_pausa: bool = False):
    """
    Guarda el estado actual de la sesión de trabajo (registro activo).

    :param registro: Objeto Registro activo
    :param en_pausa: Indica si está en pausa manual
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sesion_activa")  # Solo una sesión a la vez

    cursor.execute("""
        INSERT INTO sesion_activa (id, registro_id, proyecto_id, fecha, inicio, en_pausa)
        VALUES (1, ?, ?, ?, ?, ?)
    """, (
        registro.id,
        registro.proyecto_id,
        str(registro.fecha),
        registro.inicio.isoformat(),
        int(en_pausa)
    ))

    conn.commit()
    conn.close()

def cargar_estado_sesion() -> dict | None:
    """
    Recupera el estado de sesión guardado (si existe).
    :return: Diccionario con los datos o None si no hay sesión activa.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT registro_id, proyecto_id, fecha, inicio, en_pausa FROM sesion_activa")
    fila = cursor.fetchone()

    conn.close()

    if fila:
        registro_id, proyecto_id, fecha_str, inicio_str, en_pausa = fila
        return {
            "registro_id": registro_id,
            "proyecto_id": proyecto_id,
            "fecha": date.fromisoformat(fecha_str),
            "inicio": datetime.fromisoformat(inicio_str),
            "en_pausa": bool(en_pausa)
        }
    return None

def borrar_estado_sesion():
    """
    Elimina el registro de sesión activa (se usa al finalizar jornada).
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sesion_activa")
    conn.commit()
    conn.close()
