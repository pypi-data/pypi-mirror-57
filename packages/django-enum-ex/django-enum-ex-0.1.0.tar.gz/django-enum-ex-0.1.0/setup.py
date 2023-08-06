# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['django_enum_ex']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2,<3.0']

setup_kwargs = {
    'name': 'django-enum-ex',
    'version': '0.1.0',
    'description': '一个基于 Django 3.0 Choices 枚举类型的独立包',
    'long_description': None,
    'author': 'codetalks',
    'author_email': 'banxi1988@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
