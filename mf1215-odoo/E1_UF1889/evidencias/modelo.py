
from odoo import fields, models


class SeguimientoCliente(models.Model):
    _name = 'seguimiento.cliente'
    _description = 'Seguimiento comercial de clientes'
    _order = 'fecha desc, id desc'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    cliente_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required=True
    )

    fecha = fields.Date(
        string='Fecha',
        required=True,
        default=fields.Date.context_today
    )

    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('realizado', 'Realizado'),
        ],
        string='Estado',
        required=True,
        default='pendiente'
    )

    notas = fields.Text(string='Notas')

    def action_marcar_realizado(self):
        for registro in self:
            registro.estado = 'realizado'
