# ✅ Resumen Fase 3.2 – Casos de Uso (`core/usecases/`)

Esta sección recoge todos los casos de uso implementados en la lógica del sistema TimeTrack, basados en Clean Architecture.

---

## 🧠 ¿Qué es un caso de uso?

Un caso de uso:

- Representa **una acción real que el usuario puede realizar**
- Aplica **reglas de negocio**
- Orquesta entidades (`Proyecto`, `Registro`, `Pausa`)
- **No accede directamente a BD, GUI ni exporta nada**
- Devuelve resultados que otras capas (GUI, infraestructura) usan

---

## 📦 Casos de uso implementados

---

### 1. `iniciar_registro(proyecto_id: int) -> Registro`

📁 `core/usecases/iniciar_registro.py`

- Crea un nuevo `Registro` con la hora actual como inicio.
- No guarda en base de datos, sólo devuelve el objeto listo.

---

### 2. `cambiar_proyecto(registro_actual, nuevo_proyecto_id) -> tuple[Registro, Registro]`

📁 `core/usecases/cambiar_proyecto.py`

- Finaliza el registro actual (marcando hora de fin).
- Crea un nuevo registro para el proyecto nuevo.
- Valida que no sea el mismo proyecto.
- Devuelve ambos registros: el cerrado y el nuevo.

---

### 3. `finalizar_jornada(registro_actual: Registro) -> Registro`

📁 `core/usecases/finalizar_jornada.py`

- Marca como finalizado el registro actual.
- Valida que no esté ya cerrado.
- Devuelve el objeto actualizado para guardar o mostrar.

---

### 4. `registrar_pausa(registro_id: int, inicio: datetime, fin: datetime) -> Pausa`

📁 `core/usecases/registrar_pausa.py`

- Crea una pausa asociada a un registro activo.
- Valida que `inicio < fin` (lo hace la entidad `Pausa`).
- Devuelve el objeto `Pausa` listo para ser guardado.

---

### 5. `consultar_registros_por_fecha(fecha, registros, pausas) -> dict`

📁 `core/usecases/consultar_registros_por_fecha.py`

- Filtra todos los `Registro` y `Pausa` de una fecha dada.
- Devuelve un diccionario con las listas correspondientes.
- No hace búsquedas ni accede a BD, sólo opera sobre listas existentes.

---

### 6. `obtener_resumen_diario(fecha, registros, pausas, proyectos_por_id) -> dict`

📁 `core/usecases/obtener_resumen_diario.py`

- Calcula cuánto tiempo se trabajó en cada proyecto en un día específico.
- Agrupa el trabajo y pausas por proyecto.
- Devuelve un resumen listo para mostrar o exportar.

---

## 📌 Estado final

| Usecase                    | Estado      |
|-----------------------------|-------------|
| `iniciar_registro`          | ✅ Completo |
| `cambiar_proyecto`          | ✅ Completo |
| `finalizar_jornada`         | ✅ Completo |
| `registrar_pausa`           | ✅ Completo |
| `consultar_registros_por_fecha` | ✅ Completo |
| `obtener_resumen_diario`    | ✅ Completo |

---
