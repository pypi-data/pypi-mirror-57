# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dutch_words']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dutch-words',
    'version': '0.2.1',
    'description': '',
    'long_description': '=========================================================\nDutch word list\n=========================================================\nA simple python package that exports a list of 10,000 Dutch words ranked by usage.\n\nUsage\n=====\n``\nimport dutch_words\nwords = dutch_words.get_ranked()\n``\n',
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
