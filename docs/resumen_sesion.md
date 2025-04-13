# 💾 Resumen Módulo de Sesión Activa (`estado_sesion.py`)

Este módulo gestiona la persistencia del estado de la jornada de trabajo en curso.  
Permite recuperar automáticamente la sesión activa ante un cierre inesperado del programa, apagado del sistema o reinicio del equipo.

---

## 📦 Ubicación

📁 `src/infrastructure/storage/estado_sesion.py`

---

## 🧠 Propósito

Garantizar que el sistema pueda:

- Recordar si hay una jornada activa sin finalizar.
- Saber si el usuario estaba en pausa al cerrar la app.
- Restaurar el `Registro` y `Pausa` activos al abrir el programa.
- Eliminar el estado temporal una vez se finaliza correctamente la jornada.

---

## 🗃️ Tablas gestionadas en SQLite

### `sesion_activa`

| Campo        | Tipo      | Descripción                                      |
|--------------|-----------|--------------------------------------------------|
| `id`         | INTEGER   | Siempre será 1 (sólo una sesión a la vez)        |
| `registro_id`| INTEGER   | ID del registro de trabajo activo                |
| `proyecto_id`| INTEGER   | ID del proyecto asociado                         |
| `fecha`      | TEXT      | Fecha de la jornada (`YYYY-MM-DD`)              |
| `inicio`     | TEXT      | Fecha y hora de inicio del registro (`ISO`)     |
| `en_pausa`   | INTEGER   | 0 o 1 → indica si estaba en pausa manual         |

---

## ⚙️ Funciones disponibles

### `crear_tablas_sesion()`
- Crea las tablas necesarias (`sesion_activa`, `pausa_temporal`) si no existen.

### `guardar_estado_sesion(registro, en_pausa=False)`
- Guarda el estado actual del registro en curso.
- Opción para indicar si el estado era de pausa activa.

### `cargar_estado_sesion() -> dict | None`
- Devuelve un diccionario con los datos de sesión guardada.
- Si no hay nada, devuelve `None`.

### `borrar_estado_sesion()`
- Elimina cualquier estado de sesión guardado.
- Se recomienda usarlo al **finalizar jornada** o cuando el usuario **decida no restaurar**.

---

## 📍 Ejemplo de uso

```python
from infrastructure.storage.estado_sesion import *

crear_tablas_sesion()

# Guardar sesión en curso
guardar_estado_sesion(registro_actual, en_pausa=True)

# Al reiniciar app
sesion = cargar_estado_sesion()
if sesion:
    print("Sesión encontrada:", sesion)

# Finalizar correctamente
borrar_estado_sesion()
```

---

## 🧠 ¿Por qué no se guarda en memoria?

Porque si el sistema se apaga, un almacenamiento en variables no sobrevive.  
Este módulo asegura **persistencia real** en la base de datos local.

---

## 🔁 Integración recomendada

- Se invoca al cerrar la GUI o si detectamos error crítico.
- Al abrir la app, se verifica si hay sesión activa → si existe, preguntar al usuario si desea reanudar.

---
