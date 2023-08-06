# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sprawl']

package_data = \
{'': ['*']}

install_requires = \
['termcolor>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'sprawl',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Levi Notik',
    'author_email': 'projects@levinotik.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
