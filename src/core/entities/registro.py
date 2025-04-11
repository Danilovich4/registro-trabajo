from datetime import datetime, date

class Registro:
    """
    Representa un bloque de trabajo sobre un proyecto en una fecha específica.
    Puede contener una o varias pausas por inactividad.
    """

    def __init__(self, proyecto_id: int, fecha: date = None, inicio: datetime = None, id: int = None, fin: datetime = None):
        """
        Inicializa un nuevo registro de trabajo.

        :param proyecto_id: ID del proyecto al que pertenece este registro.
        :param fecha: Fecha del día del registro (por defecto: hoy).
        :param inicio: Hora de inicio (por defecto: ahora).
        :param id: ID de base de datos (si ya está guardado).
        :param fin: Hora de finalización (opcional).
        """
        self.id = id
        self.proyecto_id = proyecto_id
        self.fecha = fecha if fecha else datetime.now().date()
        self.inicio = inicio if inicio else datetime.now()
        self.fin = fin

    def finalizar(self):
        """
        Marca el fin del registro con la hora actual.
        """
        self.fin = datetime.now()

    def duracion_total(self):
        """
        Calcula la duración total entre inicio y fin.
        Si el registro aún está abierto, calcula hasta ahora.

        :return: Duración en formato timedelta
        """
        fin = self.fin if self.fin else datetime.now()
        return fin - self.inicio

    def __repr__(self):
        return (f"Registro(id={self.id}, proyecto_id={self.proyecto_id}, "
                f"fecha={self.fecha}, inicio={self.inicio}, fin={self.fin})")
