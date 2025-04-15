from datetime import datetime, timedelta
from infrastructure.db.connection import get_connection

def calcular_pausas_de_registro(registro_id: int) -> timedelta:
    """
    Calcula la duración total de pausas registradas para un ID de registro.

    :param registro_id: ID del registro a consultar.
    :return: Duración total de pausas como timedelta.
    """
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
