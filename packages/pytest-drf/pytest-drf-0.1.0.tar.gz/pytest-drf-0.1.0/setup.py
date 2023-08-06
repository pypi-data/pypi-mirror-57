# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pytest_drf', 'pytest_drf.util']

package_data = \
{'': ['*']}

install_requires = \
['djangorestframework>3',
 'inflection>=0.3.1,<0.4.0',
 'pytest-assert-utils>=0.1.0,<0.2.0',
 'pytest-common-subject>=1.0,<2.0',
 'pytest-lambda>=1.1,<2.0',
 'pytest>=3.6']

entry_points = \
{'pytest11': ['fixture_order = pytest_drf.plugin']}

setup_kwargs = {
    'name': 'pytest-drf',
    'version': '0.1.0',
    'description': 'A Django REST framework plugin for pytest.',
    'long_description': None,
    'author': 'Zach "theY4Kman" Kanzler',
    'author_email': 'they4kman@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
