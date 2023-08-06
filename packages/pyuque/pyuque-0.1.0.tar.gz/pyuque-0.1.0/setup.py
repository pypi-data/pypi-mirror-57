# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyuque', 'pyuque.util']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'pyuque',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/socrateslee/pyuque',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
