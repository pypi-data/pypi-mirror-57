# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dutch_words']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dutch-words',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ramon de Jezus',
    'author_email': 'rdejezus@leukeleu.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
