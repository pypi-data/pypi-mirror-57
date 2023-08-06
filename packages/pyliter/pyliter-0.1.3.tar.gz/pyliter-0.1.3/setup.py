# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyliter', 'pyliter.resources']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'colorama>=0.4.3,<0.5.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['pyliter = pyliter.__main__:pyliter_cli']}

setup_kwargs = {
    'name': 'pyliter',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'jnyjny',
    'author_email': 'erik.oshaughnessy@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
