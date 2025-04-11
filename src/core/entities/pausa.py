from datetime import datetime

class Pausa:
    """
    Representa una pausa por inactividad detectada durante una sesión de trabajo.
    """

    def __init__(self, registro_id: int, inicio: datetime, fin: datetime, id: int = None):
        """
        Inicializa una nueva pausa.

        :param registro_id: ID del registro al que pertenece esta pausa.
        :param inicio: Momento en que comenzó la inactividad.
        :param fin: Momento en que terminó la inactividad.
        :param id: Identificador único (opcional, lo asigna la base de datos).
        """
        if inicio >= fin:
            raise ValueError("La hora de inicio debe ser anterior a la hora de fin.")

        self.id = id
        self.registro_id = registro_id
        self.inicio = inicio
        self.fin = fin

    def duracion(self):
        """
        Devuelve la duración total de la pausa como un objeto timedelta.
        """
        return self.fin - self.inicio

    def __repr__(self):
        return (f"Pausa(id={self.id}, registro_id={self.registro_id}, "
                f"inicio={self.inicio}, fin={self.fin})")
