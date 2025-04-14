# 🖥️ Resumen Interfaz Gráfica (GUI) - `ventana_principal.py`

Esta es la capa de presentación del sistema TimeTrack, implementada con **Tkinter** como interfaz de escritorio amigable y modular.

---

## 📁 Ubicación

src/presentation/gui/ventana_principal.py

---

## 🎯 Objetivo

Permitir al usuario interactuar con el sistema sin necesidad de conocimientos técnicos, controlando las siguientes acciones:

- Selección o creación de proyecto
- Inicio, pausa y finalización de jornada
- Cambio de proyecto en mitad del día
- Exportación de resumen diario en Excel
- Recuperación de sesión activa tras apagado

---

## 🧩 Componentes de la Interfaz

| Elemento         | Tipo        | Función                                                                 |
|------------------|-------------|-------------------------------------------------------------------------|
| Fecha actual     | Label       | Muestra la fecha (`YYYY-MM-DD`) del día en curso                       |
| Selector         | Combobox    | Permite elegir el proyecto activo de una lista                         |
| Crear proyecto   | Botón       | Abre un `input` para ingresar y guardar un nuevo proyecto              |
| Iniciar jornada  | Botón       | Llama a `iniciar_registro()` y activa el seguimiento                   |
| Pausar manual    | Botón       | Llama a `registrar_pausa()` y suspende el trabajo temporalmente        |
| Reanudar         | Botón       | Cierra pausa activa y reanuda el seguimiento                           |
| Cambiar proyecto | Botón       | Finaliza el registro actual y abre uno nuevo con otro proyecto         |
| Finalizar jornada| Botón       | Guarda el registro actual y limpia la sesión                           |
| Exportar resumen | Botón       | Genera un archivo `.xlsx` con resumen de trabajo del día actual        |
| Estado visual    | Label       | Informa si la jornada está activa, pausada o finalizada                |

---

## 🔄 Flujo de estados

```text
[Inicio]
   ↓
[Seleccionar o crear proyecto]
   ↓
[▶️ Iniciar jornada] ─────────┐
   ↓                         ↓
[⏸️ Pausar]   ←→  [🔁 Reanudar]
   ↓
[🔄 Cambiar proyecto]
   ↓
[⏹️ Finalizar jornada]
   ↓
[📤 Exportar resumen]
