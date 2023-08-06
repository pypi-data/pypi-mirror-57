# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['mitch_dm_mypkg']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10,<2.0', 'click>=7.0,<8.0']

setup_kwargs = {
    'name': 'mitch-dm-mypkg',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Mitch Della Marta',
    'author_email': 'mitchdellamarta@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
