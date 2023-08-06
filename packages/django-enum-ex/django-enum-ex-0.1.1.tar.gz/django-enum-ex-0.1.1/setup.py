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
    'version': '0.1.1',
    'description': '一个基于 Django 3.0 Choices 枚举类型的独立包',
    'long_description': '# django-enum-ex\n一个基于 Django 3.0 Choices 枚举类型的独立扩展包\n\n本库基于 Django 3.0 中自带的 [django.db.models.enum ](https://github.com/django/django/blob/master/django/db/models/enums.py)\n\n\n特色\n---------------\n\n- 支持将枚举字段名自设置为值. 设置值为 `enum.auto()`\n- 支持将单一值即设置为值,又设置为 `label`, 通过设置类属性 `__value_as_label__ = True`\n- 增加 `Choices.of` 方法,在将原始值转成枚举值时,支持忽略大小定. 支持没有匹配枚举值时,抛出错误.\n',
    'author': 'codetalks',
    'author_email': 'banxi1988@gmail.com',
    'url': 'https://github.com/banxi1988/django-enum-ex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
