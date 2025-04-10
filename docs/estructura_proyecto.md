# 📁 Estructura del Proyecto - TimeTrack

Este documento describe la estructura de carpetas del sistema y el propósito de cada una, siguiendo los principios de Clean Architecture.

## Estructura general

```plaintext
src/
├── core/
│   ├── entities/           # Modelos de negocio: Proyecto, Registro
│   └── usecases/           # Casos de uso: iniciar_jornada, cambiar_proyecto
│
├── infrastructure/
│   ├── db/                 # Interacción con SQLite
│   ├── monitor/            # Detección de inactividad con pynput
│   └── export/             # Exportación a Excel
│
├── presentation/
│   └── gui/                # Interfaz gráfica (Tkinter)
│
├── config/                 # Variables de configuración, rutas, constantes
├── tests/                  # Pruebas unitarias y de integración
└── main.py                 # Punto de entrada de la aplicación
```

## Objetivo de la estructura

- Separar responsabilidades en capas desacopladas.
- Facilitar pruebas y mantenibilidad.
- Permitir evolución a versiones más complejas (GUI completa, web, etc.).

---
