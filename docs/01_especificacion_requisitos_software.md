# 1. Introducción

## 1.1 Alcance del Producto

Este proyecto tiene como objetivo desarrollar una aplicación de escritorio ligera y automática para el registro de horas trabajadas. El sistema permitirá contabilizar el tiempo activo de una persona mientras trabaja frente al ordenador, pausando la contabilidad si se detecta inactividad de teclado y ratón durante un período superior a cinco minutos. 

El sistema deberá almacenar los registros en una base de datos PostgreSQL y permitir la exportación de los mismos a un archivo Excel (.xlsx) para su análisis y almacenamiento externo.

## 1.2 Valor del Producto

El valor principal del producto radica en su capacidad para:

- Automatizar el registro del tiempo real de trabajo efectivo.
- Detectar pausas automáticas sin intervención del usuario.
- Evitar errores humanos en la contabilidad de horas.
- Facilitar el seguimiento y análisis en Excel, como requiere el cliente.

Es especialmente útil para trabajadores remotos, freelancers, departamentos de RRHH y pequeñas empresas que requieran una solución sencilla, sin necesidad de sistemas complejos ni conexión permanente a internet.

## 1.3 Público Objetivo

- Freelancers y autónomos que necesitan registrar sus horas de trabajo.
- Equipos de trabajo remoto.
- Gestores de proyectos y responsables de RRHH.
- Cualquier persona que quiera medir de forma precisa su tiempo de productividad frente al ordenador.

## 1.4 Uso Previsto

El usuario ejecutará la aplicación al iniciar su jornada laboral. La aplicación comenzará a registrar el tiempo en segundo plano. Si detecta inactividad prolongada (más de 5 minutos sin uso de periféricos), descontará ese tiempo del cómputo total. El usuario podrá finalizar el registro manualmente al acabar su jornada. Posteriormente, podrá consultar o exportar el informe generado.

## 1.5 Descripción General

El software estará compuesto por los siguientes componentes clave:

- Módulo de control del tiempo (inicio/parada).
- Módulo de detección de inactividad (uso de ratón y teclado).
- Persistencia de datos en PostgreSQL.
- Exportación a Excel.
- Interfaz de usuario mínima (CLI o GUI básica).
- Documentación y configuración accesible para usuarios sin conocimientos técnicos.