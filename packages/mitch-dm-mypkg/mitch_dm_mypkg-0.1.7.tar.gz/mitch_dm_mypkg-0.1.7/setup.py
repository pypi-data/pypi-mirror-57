# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['mitch_dm_mypkg', 'mitch_dm_mypkg.shusayer']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10,<2.0', 'click>=7.0,<8.0', 'cowsay>=2.0,<3.0']

entry_points = \
{'console_scripts': ['shusays = mitch_dm_mypkg.main:cli']}

setup_kwargs = {
    'name': 'mitch-dm-mypkg',
    'version': '0.1.7',
    'description': '',
    'long_description': None,
    'author': 'Mitch Della Marta',
    'author_email': 'mitchdellamarta@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
