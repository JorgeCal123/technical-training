{
    'name': 'school',  # The name that will appear in the App list
    'version': '16.0.0',  # Version
    'application': True,  # This line says the module is an App, and not a module
    'depends': ['base'],  # dependencies
    'data': [
    #    'security/groups.xml',
    #    'security/rules.xml',
    #    'security/actions.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
