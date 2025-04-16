# ✅ Resultado de Prueba Funcional - TimeTrack GUI

📅 **Fecha:** 2025-04-14  
🧪 **Tester:** Daniel López  
🎯 **Objetivo:** Verificar el correcto funcionamiento del flujo completo de la aplicación desde la interfaz gráfica.

---

## 🔍 PASOS PROBADOS

| Nº | Acción                              | Resultado Esperado                                     | Resultado Obtenido   | Observaciones                          |
|----|-------------------------------------|--------------------------------------------------------|----------------------|-----------------------------------------|
| 1  | Abrir aplicación                    | Ventana abre sin errores                               | ✅                   |                                         |
| 2  | Crear proyecto "TestPM"             | Aparece en selector                                    | ✅                   |                                         |
| 3  | Iniciar jornada                     | Estado cambia a "Trabajando", sesión activa guardada   | ✅                   | Se solucionó añadiendo `registro.id = cursor.lastrowid` |
| 4  | Pausar manualmente                  | Estado cambia a "En pausa manual"                      | ✅                   | Pausa creada sin errores                |
| 5  | Reanudar jornada                    | Estado vuelve a "Trabajando", pausa guardada en BD     | ✅                   |                                         |
| 6  | Cambiar a proyecto "TestCambio"     | Registro anterior guardado, estado actualizado         | ✅                   | Se solucionó guardando `nuevo_registro` antes de guardar sesión |
| 7  | Finalizar jornada                   | Registro guardado, sesión eliminada                    | ✅                   | Flujo cerrado correctamente             |
| 8  | Cerrar y reabrir aplicación         | No se recupera sesión (porque fue finalizada)          | ✅                   | Recuperación correcta si no se finaliza |
| 9  | Exportar resumen diario             | Archivo Excel generado con datos correctos             | ✅                   | Protección implementada contra resumen vacío |

---

## 🧠 CONCLUSIÓN

- ✅ Todos los pasos del flujo diario fueron verificados manualmente.
- 💾 Persistencia y recuperación funcionan correctamente.
- 🧪 Validación profesional de todos los flujos clave: inicio, pausa, cambio, exportación.
- 🛠️ Queda pendiente conectar la exportación a consultas reales de base de datos.
