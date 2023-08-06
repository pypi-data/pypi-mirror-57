# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
#   Vincent Van Rossem <vincent@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': "Stock Picking Copy Quantity",

    'summary': """
        Adds a button to copy reserved quantity to received quantity    
    """,

    'author': "Coop IT Easy SCRL fs",
    'website': "https://github.com/coopiteasy/addons",

    'category': 'Sales Management',
    'version': '12.0.1.0.0',

    'depends': [
        'stock',
    ],

    # always loaded
    'data': [
        'views/stock.xml',
    ],

    'demo': [],

    'installable': True
}
