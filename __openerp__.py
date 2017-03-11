# -*- coding: utf-8 -*-
{
    'name': "Inscripcion",

    'summary': """
        """,

    'description': """
        """,

    'author': "Inscripcion jacob",
    'website': "http://www.jacobjacobinscripcion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view/view_inscripcion.xml',
        'view/view_libro.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
