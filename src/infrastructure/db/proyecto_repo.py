from core.entities.proyecto import Proyecto
from infrastructure.db.connection import get_connection
from datetime import datetime

def crear_tabla_proyectos():
    """
    Crea la tabla 'proyectos' si no existe.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proyectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha_creado TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insertar_proyecto(proyecto: Proyecto):
    """
    Inserta un objeto Proyecto en la base de datos.

    :param proyecto: Instancia de Proyecto
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO proyectos (nombre, fecha_creado)
        VALUES (?, ?)
    """, (
        proyecto.nombre,
        proyecto.fecha_creado.isoformat()
    ))

    conn.commit()
    conn.close()

def obtener_todos_los_proyectos() -> list[Proyecto]:
    """
    Devuelve una lista de objetos Proyecto existentes en la BD.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, fecha_creado FROM proyectos")
    filas = cursor.fetchall()

    proyectos = []
    for fila in filas:
        id, nombre, fecha_str = fila
        fecha = datetime.fromisoformat(fecha_str).date()
        proyectos.append(Proyecto(id=id, nombre=nombre, fecha_creado=fecha))

    conn.close()
    return proyectos
