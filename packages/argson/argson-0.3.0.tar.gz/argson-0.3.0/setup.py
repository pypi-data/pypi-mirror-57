# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argson']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'argson',
    'version': '0.3.0',
    'description': 'Declare program arguments from JSON',
    'long_description': None,
    'author': 'Gabriel Chamon Araujo',
    'author_email': 'gchamon@live.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
