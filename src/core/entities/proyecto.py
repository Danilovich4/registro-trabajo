from datetime import datetime

class Proyecto:
    """
    Representa un proyecto sobre el cual se pueden registrar jornadas de trabajo.

    Esta clase forma parte de la capa de entidades (Entities),
    y contiene solo reglas del negocio puras, sin dependencias externas.
    """

    def __init__(self, nombre: str, fecha_creado: datetime.date = None, id: int = None):
        """
        Inicializa un nuevo proyecto.

        :param nombre: Nombre del proyecto, no puede estar vacío.
        :param fecha_creado: Fecha en que se creó el proyecto (por defecto: hoy).
        :param id: Identificador único (lo asigna la base de datos).
        """
        # Normalización: limpiamos el nombre
        nombre_normalizado = nombre.strip().lower()

        # Validación de regla de negocio: el proyecto debe tener nombre válido
        if not nombre_normalizado:
            raise ValueError("El nombre del proyecto no puede estar vacío.")

        self.id = id
        self.nombre = nombre_normalizado
        self.fecha_creado = fecha_creado if fecha_creado else datetime.now().date()

    def __str__(self):
        """
        Representación legible para el usuario final (GUI o Excel).
        """
        return f"{self.nombre} (creado: {self.fecha_creado})"

    def __repr__(self):
        """
        Representación técnica para desarrolladores (debug, consola, logs).
        """
        return f"Proyecto(id={self.id}, nombre='{self.nombre}', fecha_creado={self.fecha_creado})"
