# 🗂️ Resumen de Repositorios de Datos - TimeTrack

Este documento resume los módulos de infraestructura encargados de gestionar la persistencia de datos en la base SQLite utilizada por TimeTrack. Cada repositorio implementa una única responsabilidad (SRP), y se apoya en la conexión centralizada a la base de datos definida en `connection.py`.

---

## 🔌 Conexión general a SQLite

📁 `infrastructure/db/connection.py`

- Gestiona la conexión a la base de datos `timetrack.db`
- Usa `Path` y `sys` para guardar el archivo junto al `.exe` o `main.py`
- Función expuesta: `get_connection()`

---

## 🗃️ Repositorios

---

### 📁 `registro_repo.py`

#### Funciones 1

- `crear_tabla_registros()`
  - Crea la tabla `registros` si no existe.
  - Define campos: `id`, `proyecto_id`, `fecha`, `inicio`, `fin`, `tiempo_total`, `pausas_total`.

- `guardar_registro(registro)`
  - Inserta un objeto `Registro` en la BD.
  - Convierte `datetime` a formato ISO y `timedelta` a string.

---

### 📁 `pausa_repo.py`

#### Funciones 2

- `crear_tabla_pausas()`
  - Crea la tabla `pausas` si no existe.
  - Cada pausa está asociada a un `registro_id` (clave foránea).

- `guardar_pausa(pausa)`
  - Inserta una pausa detectada en la base de datos.
  - Guarda `inicio` y `fin` como texto ISO.

---

### 📁 `proyecto_repo.py`

#### Funciones 3

- `crear_tabla_proyectos()`
  - Crea la tabla `proyectos` con `id`, `nombre`, y `fecha_creado`.

- `insertar_proyecto(proyecto)`
  - Guarda un nuevo objeto `Proyecto`.

- `obtener_todos_los_proyectos()`
  - Devuelve todos los proyectos como objetos `Proyecto`.
  - Útil para menús de selección o generación de resúmenes.

---

## 🔁 Relación entre entidades

- `Proyecto` → tiene muchos `Registro`
- `Registro` → puede tener muchas `Pausa`
- `Pausa` → pertenece a un `Registro`

---

## 🧠 Buenas prácticas aplicadas

- Cada módulo gestiona **una tabla concreta**.
- Las funciones son **cohesivas y reutilizables**.
- Uso de **formato ISO** para fechas y horas (`.isoformat()`).
- Las fechas se manejan como `datetime.date` en las entidades.

---
