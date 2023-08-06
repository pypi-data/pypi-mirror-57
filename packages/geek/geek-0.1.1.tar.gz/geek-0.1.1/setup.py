# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geek']

package_data = \
{'': ['*'], 'geek': ['characters/*']}

install_requires = \
['python-slugify>=4.0.0,<5.0.0']

entry_points = \
{'console_scripts': ['geek = geek.console:run']}

setup_kwargs = {
    'name': 'geek',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Vlad Dmitrievich',
    'author_email': 'me@2tunnels.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
