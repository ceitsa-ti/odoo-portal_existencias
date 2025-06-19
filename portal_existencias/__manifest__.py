{
    'name': 'Portal Existencias',
    'version': '1.0',
    'summary': 'Módulo para mostrar existencias a usuarios tipo portal',
    'sequence': 10,
    'author': 'CEITSA',
    'website': 'https://www.ceitsa.com',
    'license': 'LGPL-3',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/portal_stock_template.xml',
        'views/portal_stock_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

