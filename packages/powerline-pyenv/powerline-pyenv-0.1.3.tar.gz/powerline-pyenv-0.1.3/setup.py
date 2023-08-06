# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['powerline_pyenv']

package_data = \
{'': ['*']}

install_requires = \
['powerline-status>=2.7,<3.0']

setup_kwargs = {
    'name': 'powerline-pyenv',
    'version': '0.1.3',
    'description': 'A Powerline segment for showing pyenv version',
    'long_description': None,
    'author': 'Sinkerine',
    'author_email': 'github@15cm.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7,<4',
}


setup(**setup_kwargs)
