# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magiconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'magiconf',
    'version': '0.1.3',
    'description': 'A small library to automagically load and parse configuration from either environment, configuration file or command line arguments.',
    'long_description': None,
    'author': 'Vladimir Kotikov',
    'author_email': 'kotikov.vladimir@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
