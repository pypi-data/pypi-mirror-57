# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyrbi']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'pyrbi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Felipe Rodrigues',
    'author_email': 'felipe@felipevr.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
