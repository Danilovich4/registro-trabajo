# ESPECIFICACIONES Y REQUISITOS

## 1. Introducción

### 1.1 Alcance del Producto

Este proyecto tiene como objetivo desarrollar una aplicación de escritorio ligera y automática para el registro de horas trabajadas. El sistema permitirá contabilizar el tiempo activo de una persona mientras trabaja frente al ordenador, pausando la contabilidad si se detecta inactividad de teclado y ratón durante un período superior a cinco minutos.

El sistema deberá almacenar los registros en una base de datos PostgreSQL y permitir la exportación de los mismos a un archivo Excel (.xlsx) para su análisis y almacenamiento externo.

### 1.2 Valor del Producto

El valor principal del producto radica en su capacidad para:

- Automatizar el registro del tiempo real de trabajo efectivo.
- Detectar pausas automáticas sin intervención del usuario.
- Evitar errores humanos en la contabilidad de horas.
- Facilitar el seguimiento y análisis en Excel, como requiere el cliente.

Es especialmente útil para trabajadores remotos, freelancers, departamentos de RRHH y pequeñas empresas que requieran una solución sencilla, sin necesidad de sistemas complejos ni conexión permanente a internet.

### 1.3 Público Objetivo

- Freelancers y autónomos que necesitan registrar sus horas de trabajo.
- Equipos de trabajo remoto.
- Gestores de proyectos y responsables de RRHH.
- Cualquier persona que quiera medir de forma precisa su tiempo de productividad frente al ordenador.

### 1.4 Uso Previsto

El usuario ejecutará la aplicación al iniciar su jornada laboral. La aplicación comenzará a registrar el tiempo en segundo plano. Si detecta inactividad prolongada (más de 5 minutos sin uso de periféricos), descontará ese tiempo del cómputo total. El usuario podrá finalizar el registro manualmente al acabar su jornada. Posteriormente, podrá consultar o exportar el informe generado.

### 1.5 Descripción General

El software estará compuesto por los siguientes componentes clave:

- Módulo de control del tiempo (inicio/parada).
- Módulo de detección de inactividad (uso de ratón y teclado).
- Persistencia de datos en PostgreSQL.
- Exportación a Excel.
- Interfaz de usuario mínima (CLI o GUI básica).
- Documentación y configuración accesible para usuarios sin conocimientos técnicos.

## 2. Requisitos Funcionales

A continuación, se describen las funciones principales que el sistema debe realizar para cumplir con los objetivos definidos.

### RF-01: Registro de jornada

El sistema deberá permitir iniciar y finalizar manualmente la jornada de trabajo mediante una interfaz básica (CLI o GUI). Al iniciar, comenzará a contar el tiempo trabajado.

### RF-02: Selección de proyecto

Al iniciar la jornada, el usuario deberá seleccionar el proyecto en el que va a trabajar, a partir de una lista existente o ingresando uno nuevo. Todos los tiempos registrados durante ese periodo se asociarán al proyecto seleccionado.
El usuario podrá cambiar de proyecto en cualquier momento durante la jornada. Al hacerlo, el sistema finalizará automáticamente el registro del proyecto anterior (guardando la hora de fin) y comenzará un nuevo registro asociado al nuevo proyecto desde el momento del cambio.

### RF-03: Detección de inactividad

El sistema deberá monitorear la actividad del teclado y ratón. Si no se detecta actividad durante un periodo superior a 5 minutos, el sistema pausará el conteo de tiempo trabajado y descontará el tiempo inactivo al reanudar.

### RF-04: Persistencia de datos

Toda la información del registro de jornada deberá almacenarse en una base de datos local SQLite, incluyendo: proyecto activo, fecha, hora de inicio, hora de fin, tiempo efectivo trabajado, y pausas detectadas.

El sistema generará un archivo `timetrack.db` que se ubicará junto al ejecutable y contendrá todos los registros de trabajo del usuario.

### RF-05: Exportación a Excel

El sistema deberá permitir exportar los registros de jornada a un archivo Excel (.xlsx), con separación por proyectos y fechas, a partir de los datos almacenados en la base de datos SQLite.

### RF-06: Visualización de resumen

El sistema deberá permitir al usuario consultar un resumen diario o por proyecto de sus horas trabajadas y pausas.

---

## 3. Requisitos de la Interfaz Externa

### 3.1 Requisitos de la interfaz de usuario

- La interfaz será sencilla, basada en una **GUI básica** (interfaz gráfica de usuario) desde la primera versión del producto. Permitirá acciones como: iniciar y finalizar jornada, seleccionar proyecto, exportar registros y consultar resúmenes.
- La interfaz deberá ser intuitiva y diseñada para usuarios sin experiencia técnica.
- En futuras versiones se podrá evaluar una migración a una versión web si se requiere acceso multiplataforma o trabajo en la nube.

### 3.2 Requisitos de la interfaz de hardware

- El sistema debe funcionar en ordenadores con sistema operativo Windows.
- Deberá acceder a dispositivos de entrada como teclado y ratón para detectar actividad.

### 3.3 Requisitos de la interfaz de software

- Interfaz con base de datos SQLite para almacenar registros de jornada, pausas y proyectos.
- Librerías de Python para:
  - Detección de periféricos (`pynput`)
  - Manipulación de fechas y tiempos (`datetime`)
  - Exportación a Excel (`pandas`, `openpyxl`)
  - Acceso a base de datos (`sqlite3`)

### 3.4 Requisitos de la interfaz de comunicación

- No se requiere conexión a internet.
- No se prevén servicios externos ni APIs en esta primera versión.

---

## 4. Requisitos No Funcionales

### 4.1 Seguridad

- Los datos registrados deben almacenarse localmente sin exposición a internet.
- Se debe evitar pérdida de datos ante cierres inesperados.
- El sistema deberá generar automáticamente una copia de seguridad de los registros activos cada 30 minutos mientras esté en funcionamiento. Estas copias de seguridad se guardarán en un archivo local adicional (por ejemplo, en formato JSON o SQLite ligero), que podrá ser restaurado en caso de fallo inesperado.

### 4.2 Capacidad

- Se podrán almacenar múltiples registros históricos sin límite específico.
- Deberá permitir guardar múltiples proyectos.

### 4.3 Compatibilidad

- Compatible con Windows 10 y superiores.
- Requiere Python 3.10+ para el desarrollo.
- El programa final podrá ser ejecutado como `.exe` sin necesidad de instalar dependencias ni sistemas de base de datos externos.

### 4.4 Confiabilidad

- El sistema debe garantizar que no se registren pausas erróneas por breves momentos sin actividad (tolerancia mínima: 5 minutos exactos).

### 4.5 Escalabilidad

- El sistema debe permitir en futuras versiones incluir:
  - GUI completa
  - Gestión avanzada de proyectos
  - Análisis de rendimiento personal
  - Exportación automática semanal

### 4.6 Mantenibilidad

- El sistema se desarrollará siguiendo principios de Clean Architecture para facilitar mantenibilidad y extensión modular.

### 4.7 Facilidad de uso

- Pensado para usuarios sin experiencia técnica.
- No requiere instalación compleja.

### 4.8 Otros requisitos no funcionales

- Código fuente documentado.
- Proyecto versionado con Git (GitHub), incluyendo ramas `main` y `dev`.
- La base de datos SQLite se almacenará localmente en un archivo `.db`, que acompañará al ejecutable final (`.exe`).
- La aplicación será entregada en formato ejecutable para facilitar su uso por usuarios sin conocimientos técnicos.
- El sistema será auto-contenido, sin necesidad de instalación de PostgreSQL, Python o librerías externas.
