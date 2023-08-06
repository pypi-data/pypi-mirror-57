# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['jsonbourne']
setup_kwargs = {
    'name': 'jsonbourne',
    'version': '0.1.1',
    'description': 'Import the best JSON lib',
    'long_description': None,
    'author': 'jesse',
    'author_email': 'jesse@dgi.com',
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
