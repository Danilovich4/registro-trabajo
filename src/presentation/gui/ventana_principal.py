import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from datetime import date, datetime

# ENTITIES y USECASES
from core.entities.proyecto import Proyecto
from core.entities.registro import Registro

from core.usecases.iniciar_registro import iniciar_registro
from core.usecases.finalizar_jornada import finalizar_jornada
from core.usecases.cambiar_proyecto import cambiar_proyecto
from core.usecases.registrar_pausa import registrar_pausa
from core.usecases.obtener_resumen_diario import obtener_resumen_diario

# INFRAESTRUCTURA
from infrastructure.db.proyecto_repo import (
    crear_tabla_proyectos,
    insertar_proyecto,
    obtener_todos_los_proyectos
)
from infrastructure.db.registro_repo import crear_tabla_registros, guardar_registro
from infrastructure.db.pausa_repo import crear_tabla_pausas, guardar_pausa

from infrastructure.storage.estado_sesion import (
    crear_tablas_sesion,
    guardar_estado_sesion,
    borrar_estado_sesion,
    cargar_estado_sesion
)

from infrastructure.export.excel_exporter import exportar_resumen_diario_a_excel


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("TimeTrack - Registro de Jornada")
        self.root.geometry("520x420")

        self.proyectos = []
        self.proyecto_actual = None
        self.registro_actual = None
        self.pausa_actual = None

        crear_tabla_proyectos()
        crear_tabla_registros()
        crear_tabla_pausas()
        crear_tablas_sesion()

        self.label_fecha = tk.Label(root, text=f"📅 Fecha: {date.today()}", font=("Arial", 12))
        self.label_fecha.pack(pady=5)

        self.selector_proyecto = ttk.Combobox(root, state="readonly", width=40)
        self.selector_proyecto.pack()

        self.btn_nuevo_proyecto = tk.Button(root, text="➕ Crear nuevo proyecto", command=self.crear_nuevo_proyecto)
        self.btn_nuevo_proyecto.pack(pady=5)

        self.btn_iniciar = tk.Button(root, text="▶️ Iniciar jornada", command=self.iniciar_jornada)
        self.btn_iniciar.pack(pady=5)

        self.btn_pausar = tk.Button(root, text="⏸️ Pausar manualmente", command=self.pausar_manual)
        self.btn_pausar.pack(pady=5)

        self.btn_reanudar = tk.Button(root, text="🔁 Reanudar", command=self.reanudar)
        self.btn_reanudar.pack(pady=5)

        self.btn_cambiar = tk.Button(root, text="🔄 Cambiar proyecto", command=self.cambiar_proyecto)
        self.btn_cambiar.pack(pady=5)

        self.btn_finalizar = tk.Button(root, text="⏹️ Finalizar jornada", command=self.finalizar_jornada)
        self.btn_finalizar.pack(pady=5)

        self.btn_exportar = tk.Button(root, text="📤 Exportar resumen a Excel", command=self.exportar_excel)
        self.btn_exportar.pack(pady=5)

        self.label_estado = tk.Label(root, text="Estado: Sin iniciar", font=("Arial", 10), fg="gray")
        self.label_estado.pack(pady=10)

        self.cargar_proyectos()
        self.recuperar_sesion_anterior()

    def cargar_proyectos(self):
        self.proyectos = obtener_todos_los_proyectos()
        nombres = [p.nombre for p in self.proyectos]
        self.selector_proyecto['values'] = nombres
        if nombres:
            self.selector_proyecto.current(0)

    def crear_nuevo_proyecto(self):
        nombre = simpledialog.askstring("Nuevo proyecto", "Introduce el nombre del nuevo proyecto:")
        if nombre:
            nuevo = Proyecto(nombre=nombre)
            insertar_proyecto(nuevo)
            self.cargar_proyectos()
            messagebox.showinfo("Proyecto creado", f"Proyecto '{nombre}' añadido con éxito.")

    def iniciar_jornada(self):
        if self.registro_actual:
            messagebox.showwarning("Jornada activa", "Ya hay una jornada iniciada.")
            return

        seleccionado = self.selector_proyecto.get()
        if not seleccionado:
            messagebox.showwarning("Proyecto requerido", "Debes seleccionar un proyecto.")
            return

        for proyecto in self.proyectos:
            if proyecto.nombre == seleccionado:
                self.proyecto_actual = proyecto
                break

        self.registro_actual = iniciar_registro(self.proyecto_actual.id)
        guardar_estado_sesion(self.registro_actual, en_pausa=False)

        self.label_estado.config(text=f"✅ Trabajando en '{self.proyecto_actual.nombre}'", fg="green")

    def pausar_manual(self):
        if not self.registro_actual or self.pausa_actual:
            return

        self.pausa_actual = registrar_pausa(
            registro_id=self.registro_actual.id,
            inicio=datetime.now(),
            fin=datetime.now()  # se ajusta al final
        )
        self.pausa_actual.fin = None
        guardar_estado_sesion(self.registro_actual, en_pausa=True)

        self.label_estado.config(text="⏸️ En pausa manual", fg="orange")

    def reanudar(self):
        if not self.pausa_actual or not self.registro_actual:
            return

        self.pausa_actual.fin = datetime.now()
        guardar_pausa(self.pausa_actual)
        self.pausa_actual = None
        guardar_estado_sesion(self.registro_actual, en_pausa=False)

        self.label_estado.config(text=f"✅ Reanudado en '{self.proyecto_actual.nombre}'", fg="green")

    def cambiar_proyecto(self):
        if not self.registro_actual:
            messagebox.showwarning("No hay jornada activa", "Inicia una jornada antes de cambiar de proyecto.")
            return

        seleccionado = self.selector_proyecto.get()
        if not seleccionado or seleccionado == self.proyecto_actual.nombre:
            messagebox.showwarning("Proyecto inválido", "Selecciona un proyecto diferente al actual.")
            return

        for proyecto in self.proyectos:
            if proyecto.nombre == seleccionado:
                nuevo_proyecto = proyecto
                break

        registro_final, nuevo_registro = cambiar_proyecto(self.registro_actual, nuevo_proyecto.id)
        guardar_registro(registro_final)

        self.registro_actual = nuevo_registro
        self.proyecto_actual = nuevo_proyecto
        guardar_estado_sesion(self.registro_actual, en_pausa=False)

        self.label_estado.config(text=f"✅ Cambiado a '{self.proyecto_actual.nombre}'", fg="blue")

    def finalizar_jornada(self):
        if not self.registro_actual:
            return

        registro_final = finalizar_jornada(self.registro_actual)
        guardar_registro(registro_final)
        borrar_estado_sesion()

        self.registro_actual = None
        self.pausa_actual = None
        self.label_estado.config(text="🛑 Jornada finalizada", fg="red")

    def exportar_excel(self):
        if not self.proyectos:
            messagebox.showinfo("Sin proyectos", "No hay proyectos cargados para exportar.")
            return

        proyectos_por_id = {p.id: p.nombre for p in self.proyectos}
        registros = []  # Se conectará más adelante a BD real
        pausas = []

        resumen = obtener_resumen_diario(
            fecha=date.today(),
            registros=registros,
            pausas=pausas,
            proyectos_por_id=proyectos_por_id
        )

        exportar_resumen_diario_a_excel(resumen)
        messagebox.showinfo("Exportación", "Resumen exportado correctamente.")

    def recuperar_sesion_anterior(self):
        datos = cargar_estado_sesion()
        if datos:
            for proyecto in self.proyectos:
                if proyecto.id == datos["proyecto_id"]:
                    self.proyecto_actual = proyecto
                    break

            self.registro_actual = Registro(
                id=datos["registro_id"],
                proyecto_id=datos["proyecto_id"],
                fecha=datos["fecha"],
                inicio=datos["inicio"]
            )

            self.selector_proyecto.set(self.proyecto_actual.nombre)

            if datos["en_pausa"]:
                self.label_estado.config(
                    text=f"⏸️ Sesión restaurada en pausa ({self.proyecto_actual.nombre})",
                    fg="orange"
                )
            else:
                self.label_estado.config(
                    text=f"✅ Sesión restaurada en curso ({self.proyecto_actual.nombre})",
                    fg="green"
                )

            messagebox.showinfo("Sesión recuperada", "Se restauró la sesión activa anterior.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
