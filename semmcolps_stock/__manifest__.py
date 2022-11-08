# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Semmcolps (Stock)',
    'summary': 'Semmcolps (Stock)',
    'sequence': 100,
    "version": "1.0",
    'website': 'https://www.odoo.com',
    'author': 'Odoo Ps',
    'description': "TASK ID - 3035161",
    'category': 'Custom Development',
    'depends': [
        'sale_management',
        'purchase',
        'stock',
        'mrp',
    ],
    'data': [
        # Datas
        'data/data.xml',
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/stock_lot_views.xml',
        'views/stock_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
