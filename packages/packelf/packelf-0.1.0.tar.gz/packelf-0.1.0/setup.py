# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['packelf']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['packelf = packelf.cli:main']}

setup_kwargs = {
    'name': 'packelf',
    'version': '0.1.0',
    'description': 'Pack ELF files in a given path to make them relocatable',
    'long_description': None,
    'author': 'Fixpoint, Inc.',
    'author_email': 'developer@fixpoint.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fixpoint/packelf',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
