# 📄 Registro de Cambios - TimeTrack

Este archivo documenta los cambios más importantes realizados en el proyecto TimeTrack, desde su planificación hasta su versión final.

---

## [v1.0.0] - 2025-04-15

### Añadido

- Interfaz gráfica (GUI) con Tkinter.
- Registro por proyecto con inicio y fin manual.
- Registro de pausas automáticas tras 5 minutos de inactividad.
- Detección de teclado y ratón con `pynput`.
- Cambio de proyecto en caliente durante la jornada.
- Exportación de datos a Excel (`.xlsx`) con `pandas` y `openpyxl`.
- Creación automática de la base de datos SQLite (`timetrack.db`).
- Recuperación de sesión activa tras reinicio.
- `README.md` profesional con tareas y tecnologías.
- Archivo `instrucciones.txt` para entrega al cliente final.
- Pruebas unitarias con `pytest` (entidades, usecases y exportador).
- Generación de ejecutable `.exe` con PyInstaller.

### Mejorado

- Validación y normalización automática del nombre de proyecto.
- Registro correcto de pausas al cambiar de proyecto estando en pausa.
- Refactor de estructura a Clean Architecture (entidades, usecases, infraestructura, presentación).
- Modularización del detector de inactividad.

### Corregido

- Error al guardar registros sin `fin`.
- Problemas con `pynput` y exportación sin columnas.
- Conflictos al cambiar de proyecto durante pausa activa.
- Evita contar tiempo pausado como trabajado.

---

## [v0.1.0] - 2025-04-08

### 🛠 Versión inicial (MVP)

- Planificación del proyecto según PMBOK.
- Documentación de requisitos con plantilla SRS.
- Script `.bat` para creación de estructura inicial.
- Diseño de arquitectura limpia y modular.
- Inicio de pruebas locales de jornada manual.
