# ✅ Resumen Fase 3.1 – Implementación de Entidades (`core/entities/`)

En esta fase se definieron las entidades clave del sistema TimeTrack, siguiendo los principios de Clean Architecture:

---

## 🧱 Principios aplicados

- Separación de responsabilidades (SRP)
- Reglas de negocio puras, sin dependencias externas
- Preparadas para usarse desde los casos de uso (`usecases/`)
- No interactúan con GUI, BD ni exportaciones directamente
- Validaciones internas para asegurar integridad

---

## 📦 Entidades implementadas

### 1. `Proyecto`

```python
Proyecto(nombre: str, fecha_creado: date = hoy, id: int = None)
```

- Representa un proyecto activo.
- Valida que el nombre no esté vacío.
- Normaliza el nombre (minúsculas y sin espacios extra).
- Incluye `__str__` para GUI y `__repr__` para desarrollo.

---

### 2. `Registro`

```python
Registro(proyecto_id: int, fecha: date = hoy, inicio: datetime = ahora, fin: datetime = None, id: int = None)
```

- Representa un bloque de trabajo en una jornada.
- Tiene fecha, hora de inicio y fin.
- Método `finalizar()` para marcar el cierre de la jornada.
- Método `duracion_total()` para calcular el tiempo trabajado.
- Solo contiene datos y lógica propia, no depende de la BD.

---

### 3. `Pausa`

```python
Pausa(registro_id: int, inicio: datetime, fin: datetime, id: int = None)
```

- Representa un periodo de inactividad.
- Valida que la hora de inicio sea anterior a la de fin.
- Método `duracion()` para obtener su duración.
- Se asocia a un `Registro` específico.

---

## 📂 Ubicación del código

```plaintext
src/
└── core/
    └── entities/
        ├── proyecto.py
        ├── registro.py
        └── pausa.py
```

---

## 📌 Próximo paso

Pasar a la **fase 3.2 – Implementación de casos de uso (`core/usecases/`)**, donde usaremos estas entidades para realizar acciones como:

- Iniciar jornada
- Cambiar de proyecto
- Finalizar jornada
- Consultar registros
