# 🗃️ Modelo de Base de Datos - TimeTrack

Este documento describe el modelo entidad-relación (ER) utilizado para almacenar los registros de trabajo, pausas e información de los proyectos en SQLite.

---

## 📐 Diagrama Entidad-Relación

```plaintext
┌──────────────┐          ┌──────────────────── ┐           ┌───────────────┐
│  proyectos   │   1   ─> │     registros       │   1   ─>  │     pausas    │
│--------------│          │---------------------│           │---------------│
│ id (PK)      │          │ id (PK)             │           │ id (PK)       │
│ nombre       │          │ proyecto_id (FK)    │           │ registro_id   │ (FK)
│ fecha_creado │          │ fecha (solo día)    │           │ inicio        │
└──────────────┘          │ inicio (fecha+hora) │           │ fin           │
                          │ fin                 │           └───────────────┘
                          │ tiempo_total        │
                          │ pausas_total        │
                          └─────────────────────┘
```

---

## 📄 Esquema SQL (adaptado a SQLite)

```sql
CREATE TABLE proyectos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha_creado TEXT NOT NULL
);

CREATE TABLE registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proyecto_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,         
    inicio TEXT NOT NULL,       
    fin TEXT,
    tiempo_total TEXT,
    pausas_total TEXT,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
);


CREATE TABLE pausas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    registro_id INTEGER NOT NULL,
    inicio TEXT NOT NULL,
    fin TEXT NOT NULL,
    FOREIGN KEY (registro_id) REFERENCES registros(id)
);
```

---

## 🔍 Explicación

### `proyectos`

- Tabla principal con el nombre del proyecto y su fecha de creación.

### `registros`

- Cada vez que el usuario trabaja en un proyecto, se crea un registro con hora de inicio y fin.
- Se calcula `tiempo_total` (sin pausas) y `pausas_total`.

### `pausas`

- Cada vez que se detecta inactividad, se registra una pausa asociada a un registro.
- Permite reconstruir y analizar el tiempo real de trabajo.

---

## 🧠 Por qué no relacionamos pausas directamente con proyectos

Cada pausa **pertenece a un bloque de trabajo concreto**, no al proyecto directamente.  
Esto permite:

- Analizar sesiones separadas.
- Calcular métricas por jornada.
- Mantener coherencia en el modelo.

---
