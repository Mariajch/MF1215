{
    'name': 'Seguimiento de clientes',
    'summary': 'Gestión del seguimiento comercial de clientes',
    'description': """
        Módulo para registrar y gestionar el seguimiento
        comercial de clientes en Odoo.
    """,
    'author': 'Maria Chirinos',
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}


