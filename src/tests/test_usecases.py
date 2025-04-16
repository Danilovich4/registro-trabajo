from datetime import datetime, timedelta
from core.entities.registro import Registro
from core.usecases.iniciar_registro import iniciar_registro
from core.usecases.finalizar_jornada import finalizar_jornada
from core.usecases.cambiar_proyecto import cambiar_proyecto

def test_iniciar_registro():
    proyecto_id = 1
    registro = iniciar_registro(proyecto_id)

    assert isinstance(registro, Registro)
    assert registro.proyecto_id == proyecto_id
    assert registro.inicio is not None
    assert registro.fin is None

def test_finalizar_jornada_agrega_fin():
    registro = iniciar_registro(1)
    registro.id = 10  # Simula que ya fue guardado en BD
    registro_finalizado = finalizar_jornada(registro)

    assert registro_finalizado.fin is not None
    assert registro_finalizado.pausas_total is not None
    assert isinstance(registro_finalizado.pausas_total, timedelta)

def test_cambiar_proyecto_genera_dos_registros():
    original = iniciar_registro(1)
    original.id = 10  # Simula que está en BD

    registro_final, nuevo_registro = cambiar_proyecto(original, nuevo_proyecto_id=2)

    assert registro_final.proyecto_id == 1
    assert registro_final.fin is not None
    assert nuevo_registro.proyecto_id == 2
    assert nuevo_registro.fin is None
