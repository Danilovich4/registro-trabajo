# 📐 Arquitectura del Sistema - TimeTrack

Este documento describe la organización del sistema según los principios de Clean Architecture. Cada capa tiene responsabilidades claramente definidas, lo que facilita el mantenimiento, escalabilidad y pruebas.

## 🧱 Diagrama general de capas

```plaintext
+----------------------------+
|    Interfaz de Usuario     |  ← GUI (Tkinter)
|  src/presentation/gui/     |
+-------------+--------------+
              ↓
+----------------------------+
|        Casos de Uso        |  ← Lógica del sistema (qué se hace)
|    src/core/usecases/      |
+-------------+--------------+
              ↓
+----------------------------+
|     Entidades del Dominio  |  ← Reglas del negocio puras
|    src/core/entities/      |
+-------------+--------------+
              ↑
+----------------------------+
|   Infraestructura Técnica  |  ← Cómo se hace (BD, Excel, input)
|    src/infrastructure/     |
+----------------------------+
```

## 🔄 Responsabilidades por capa

### `core/entities/`

- Define el **modelo del dominio** (Proyecto, Registro, etc.).
- Contiene solo atributos y métodos esenciales de las reglas de negocio.

### `core/usecases/`

- Contiene la **lógica que coordina** acciones del sistema: iniciar jornada, cambiar proyecto, exportar registros...
- No depende de infraestructura ni GUI.

### `infrastructure/`

- Implementa tecnologías concretas: base de datos, detección de input, exportación a Excel.
- Es fácilmente sustituible.

### `presentation/gui/`

- Muestra la interfaz gráfica (Tkinter).
- Se comunica solo con los casos de uso.

---
