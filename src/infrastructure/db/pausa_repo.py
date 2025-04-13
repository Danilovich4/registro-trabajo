from core.entities.pausa import Pausa
from infrastructure.db.connection import get_connection

def crear_tabla_pausas():
    """
    Crea la tabla 'pausas' si no existe.
    Cada pausa pertenece a un registro existente.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pausas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            registro_id INTEGER NOT NULL,
            inicio TEXT NOT NULL,
            fin TEXT NOT NULL,
            FOREIGN KEY (registro_id) REFERENCES registros(id)
        )
    """)

    conn.commit()
    conn.close()

def guardar_pausa(pausa: Pausa):
    """
    Guarda un objeto Pausa en la base de datos.

    :param pausa: Objeto Pausa a insertar.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pausas (registro_id, inicio, fin)
        VALUES (?, ?, ?)
    """, (
        pausa.registro_id,
        pausa.inicio.isoformat(),
        pausa.fin.isoformat()
    ))

    conn.commit()
    conn.close()
