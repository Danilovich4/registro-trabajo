from datetime import datetime, timedelta
from core.entities.registro import Registro
from core.entities.pausa import Pausa
from core.entities.proyecto import Proyecto

def test_duracion_total_registro():
    inicio = datetime(2025, 4, 14, 10, 0, 0)
    fin = datetime(2025, 4, 14, 12, 0, 0)
    registro = Registro(proyecto_id=1, inicio=inicio, fin=fin)

    assert registro.duracion_total() == timedelta(hours=2)

def test_duracion_pausa_completa():
    inicio = datetime(2025, 4, 14, 13, 0, 0)
    fin = datetime(2025, 4, 14, 13, 15, 0)
    pausa = Pausa(registro_id=1, inicio=inicio, fin=fin)

    assert pausa.duracion() == timedelta(minutes=15)

def test_proyecto_nombre_normalizado():
    proyecto = Proyecto(nombre="   Lingua TIME   ")
    assert proyecto.nombre == "lingua time"