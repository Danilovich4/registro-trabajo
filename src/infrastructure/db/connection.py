import sqlite3
from pathlib import Path
import os
import sys

def get_base_path() -> Path:
    """
    Determina la ruta base del ejecutable o del script Python.
    Esto garantiza que la base de datos esté junto al .exe o main.py.
    """
    if getattr(sys, 'frozen', False):
        # Si el programa está compilado como .exe
        return Path(sys.executable).parent
    else:
        # Si se ejecuta como script Python (.py)
        return Path(__file__).resolve().parent.parent.parent  # Sube 3 niveles hasta la raíz del proyecto

# Ruta definitiva de la base de datos
DB_PATH = get_base_path() / "timetrack.db"

def get_connection():
    """
    Devuelve una conexión a la base de datos SQLite.
    La base de datos se guarda junto al .exe o al main.py.
    """
    conn = sqlite3.connect(DB_PATH)
    return conn
