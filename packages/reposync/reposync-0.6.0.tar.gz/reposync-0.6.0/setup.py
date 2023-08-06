# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reposync']

package_data = \
{'': ['*'], 'reposync': ['scripts/*']}

install_requires = \
['fire>=0.2.1,<0.3.0', 'gitpython>=3.0.5,<4.0.0', 'pyaml>=19.12.0,<20.0.0']

setup_kwargs = {
    'name': 'reposync',
    'version': '0.6.0',
    'description': 'Organize git repositories.',
    'long_description': None,
    'author': 'Devin Alvaro',
    'author_email': 'devin.alvaro@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
