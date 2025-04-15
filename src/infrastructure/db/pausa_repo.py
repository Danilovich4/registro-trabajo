from datetime import datetime, date,timedelta
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

def obtener_pausas_por_fecha(fecha: date) -> list[Pausa]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id, p.registro_id, p.inicio, p.fin
        FROM pausas p
        JOIN registros r ON p.registro_id = r.id
        WHERE r.fecha = ?
    """, (str(fecha),))

    filas = cursor.fetchall()
    conn.close()

    pausas = []
    for fila in filas:
        id, registro_id, inicio_str, fin_str = fila
        pausas.append(Pausa(
            id=id,
            registro_id=registro_id,
            inicio=datetime.fromisoformat(inicio_str),
            fin=datetime.fromisoformat(fin_str) if fin_str else None
        ))

    return pausas

def calcular_pausas_de_registro(registro_id: int) -> timedelta:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT inicio, fin FROM pausas
        WHERE registro_id = ?
        AND fin IS NOT NULL
    """, (registro_id,))
    
    filas = cursor.fetchall()
    conn.close()

    total_pausa = timedelta()

    for inicio_str, fin_str in filas:
        inicio = datetime.fromisoformat(inicio_str)
        fin = datetime.fromisoformat(fin_str)
        total_pausa += (fin - inicio)

    return total_pausa

def obtener_todas_las_pausas() -> list[Pausa]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, registro_id, inicio, fin
        FROM pausas
        WHERE fin IS NOT NULL
    """)

    filas = cursor.fetchall()
    conn.close()

    pausas = []
    for fila in filas:
        id, registro_id, inicio_str, fin_str = fila
        pausas.append(Pausa(
            id=id,
            registro_id=registro_id,
            inicio=datetime.fromisoformat(inicio_str),
            fin=datetime.fromisoformat(fin_str)
        ))

    return pausas
