# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pytzkt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pytzkt',
    'version': '0.1.1',
    'description': 'TzKT API wrapper',
    'long_description': None,
    'author': 'AO',
    'author_email': 'aopoltorzhicky@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
