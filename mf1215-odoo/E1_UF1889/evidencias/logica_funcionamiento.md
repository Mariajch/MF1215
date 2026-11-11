# Lógica de funcionamiento — Seguimiento de clientes

## 1. Objetivo

Desarrollar un módulo personalizado en Odoo Community para registrar y gestionar el seguimiento comercial de clientes.

## 2. Modelo de datos

Se creó el modelo `seguimiento.cliente` mediante Python, utilizando `models.Model`.

Campos definidos:

- `name`: nombre del seguimiento, obligatorio.
- `cliente_id`: relación Many2one con `res.partner`, obligatoria.
- `fecha`: fecha del seguimiento, con valor predeterminado de la fecha actual.
- `estado`: selección entre Pendiente y Realizado. Su valor inicial es Pendiente.
- `notas`: campo de texto para observaciones.

## 3. Vistas y navegación

Se configuraron vistas de lista y formulario mediante XML.

Se creó el menú principal «Seguimiento de clientes», con el submenú «Seguimientos», para acceder a los registros.

## 4. Lógica del botón

Se implementó el método Python `action_marcar_realizado`.

Cuando el usuario pulsa el botón «Marcar como realizado», el método recorre los registros seleccionados y cambia el campo `estado` a `realizado`.

## 5. Seguridad

Se configuró el archivo `ir.model.access.csv` para permitir a los usuarios internos consultar, crear, modificar y eliminar registros del modelo.

## 6. Pruebas realizadas

Se creó el registro «Seguimiento comercial 001» para el cliente «Acme Corporation», con fecha 10/11/2026 y estado inicial Pendiente.

Posteriormente, se pulsó el botón «Marcar como realizado».

Se comprobó que el estado cambió correctamente a Realizado y que la modificación apareció en la vista de lista.

## 7. Resultado

El módulo se instaló en Odoo y se comprobó el funcionamiento de sus vistas, registros y botón de cambio de estado.