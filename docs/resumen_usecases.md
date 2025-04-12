# ✅ Resumen Fase 3.2 – Casos de Uso (`core/usecases/`)

Esta sección contiene los casos de uso que orquestan las acciones principales del sistema TimeTrack, según Clean Architecture.

---

## 🔁 ¿Qué es un caso de uso?

Un caso de uso:

- Representa **una acción concreta que el usuario puede realizar**
- Usa las **entities del sistema** para aplicar reglas de negocio
- **No se conecta directamente a GUI, BD, ni exportación**
- Devuelve resultados para que otra capa decida qué hacer con ellos

---

## 📦 Casos de uso implementados

---

### 1. `iniciar_registro(proyecto_id: int) -> Registro`

📁 `core/usecases/iniciar_registro.py`

- Crea un nuevo objeto `Registro` con la hora actual como inicio.
- No lo guarda, solo lo devuelve para que otras capas lo usen.
- Preparado para usarse al iniciar jornada o tras cambio de proyecto.

```python
registro = iniciar_registro(proyecto_id=1)
```

---

### 2. `cambiar_proyecto(registro_actual, nuevo_proyecto_id) -> tuple[Registro, Registro]`

📁 `core/usecases/cambiar_proyecto.py`

- Finaliza el `registro_actual`.
- Crea un nuevo `Registro` con el nuevo `proyecto_id`.
- Valida que el proyecto nuevo no sea el mismo.
- Devuelve una tupla con:
  - el registro finalizado
  - el nuevo registro iniciado

```python
registro_final, nuevo = cambiar_proyecto(registro_actual, nuevo_proyecto_id)
```

---

### 3. `finalizar_jornada(registro_actual: Registro) -> Registro`

📁 `core/usecases/finalizar_jornada.py`

- Finaliza el `registro_actual`, marcando la hora de fin.
- Valida que no esté ya finalizado.
- Devuelve el objeto actualizado para ser guardado o mostrado.

```python
registro_final = finalizar_jornada(registro_actual)
```

---

## 📌 Estado actual

| Usecase               | Estado      |
|------------------------|-------------|
| `iniciar_registro`     | ✅ Completo |
| `cambiar_proyecto`     | ✅ Completo |
| `finalizar_jornada`    | ✅ Completo |

---

## 🧠 Próximos posibles casos de uso

- `registrar_pausa`: guardar una pausa detectada en el registro activo
- `obtener_resumen`: construir resumen diario o por proyecto
- `exportar_registros`: convertir datos a Excel
- `consultar_registros_por_fecha`: para generar reportes o visualizaciones

---
