{
    'name': "College ERP",
    'version': "18.0.1.1",
    'license': "LGPL-3",
    'summary': """An erp for college education""",
    'description': """From students administration to exam , this covers all aspects of college administration""",
    'author': "Marcellius",
    'category': "Education",
    'website': "www.cybrosys.com",
    'maintainer': "Marcellius Pt Holding <marcelliusfelixmatius@gmail.com>",
    'sequence': 1,
    'data': [
        "security/ir.model.access.csv",
        "views/college_student.xml",
        "views/college_erp_menus.xml",
    ],
    'application': True,
    'auto_install': False,
    'installable': True
}