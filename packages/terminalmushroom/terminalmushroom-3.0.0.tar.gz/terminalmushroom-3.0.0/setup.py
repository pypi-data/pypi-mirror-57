# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['terminalmushroom']

package_data = \
{'': ['*']}

install_requires = \
['protobuf>=3.10,<4.0']

setup_kwargs = {
    'name': 'terminalmushroom',
    'version': '3.0.0',
    'description': '',
    'long_description': None,
    'author': 'Coriander Pines',
    'author_email': '1647914-cvpines@users.noreply.gitlab.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
