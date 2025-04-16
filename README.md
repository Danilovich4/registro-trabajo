# 🕒 TimeTrack - Registro Inteligente de Horas de Trabajo

TimeTrack es una aplicación de escritorio desarrollada en Python para registrar de forma automática y precisa las horas efectivas de trabajo por proyecto. Permite pausar la jornada manualmente o detectar inactividad (teclado/ratón) de más de 5 minutos para registrar pausas automáticas. Exporta los datos a Excel para su análisis.

---

## 🛠 Tecnologías utilizadas

- **Lenguaje de programación:** Python 3.11
- **Interfaz gráfica:** Tkinter
- **Detección de inactividad:** `pynput`
- **Base de datos:** SQLite (`timetrack.db`)
- **Exportación:** Excel (via `pandas` + `openpyxl`)
- **Pruebas automatizadas:** Pytest
- **Control de versiones:** Git + GitHub
- **Editor de desarrollo:** Visual Studio Code
- **Gestión de ramas:** `main` (producción) y `dev` (desarrollo)
- **Empaquetado:** PyInstaller para generar `.exe`
- **Gestión de tareas:** Basado en metodología PMBOK

---

## ✅ Lista de tareas y progreso

### Etapa 1 - Planificación y Documentación

- [x] Definir objetivo y alcance del proyecto
- [x] Crear estructura de carpetas Clean Architecture
- [x] Crear script `.bat` de inicialización
- [x] Crear `README.md` inicial
- [x] Documentar requisitos (PMBOK + plantilla SRS)
- [x] Diagramas y documentación técnica (`/docs`)

### Etapa 2 - Diseño Técnico

- [x] Definir arquitectura (Clean Architecture)
- [x] Diseñar modelo de datos (SQLite)
- [x] Identificar y listar librerías en `requirements.txt`
- [x] Documentar estructura del sistema y dependencias

### Etapa 3 - Desarrollo MVP

- [x] Registro por proyecto con inicio/parada manual
- [x] Detección de inactividad con pausa automática (5 min)
- [x] Gestión de múltiples proyectos por jornada
- [x] Exportación diaria completa a Excel (`.xlsx`)
- [x] Persistencia local en SQLite con recuperación de sesión

### Etapa 4 - Testing y Entrega

- [x] Pruebas unitarias con `pytest` (entidades, usecases y exportación)
- [x] Generación de ejecutable `.exe` con PyInstaller
- [x] Pruebas del `.exe` en entorno simulado cliente
- [x] Generación de archivo `instrucciones.txt`
- [x] Actualización y entrega del `README.md` final

---

## 📦 Entregables

- `registro_trabajo.exe` → ejecutable principal
- `timetrack.db` → base de datos local (se crea sola si no existe)
- `instrucciones.txt` → guía de uso para el cliente final

---

## 🧠 Sobre este proyecto

Este desarrollo se ha llevado a cabo como parte de un proyecto real de formación en Ingeniería de Software. Aplica buenas prácticas de arquitectura (Clean Architecture), diseño profesional, pruebas automatizadas y entrega funcional empaquetada.

Ha servido como un caso práctico para comprender cómo estructurar un proyecto real: desde documentación inicial hasta despliegue.

---

## 🔗 Repositorio del proyecto

[GitHub - Danilovich4/registro-trabajo](https://github.com/Danilovich4/registro-trabajo)
