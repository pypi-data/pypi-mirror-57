# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['django_fsm_ex',
 'django_fsm_ex.management',
 'django_fsm_ex.management.commands',
 'django_fsm_ex.tests']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2,<3.0']

extras_require = \
{'commands': ['graphviz>=0.10,<0.11']}

setup_kwargs = {
    'name': 'django-fsm-ex',
    'version': '3.0.0',
    'description': '一个基于 Django 有限状态管理工具库,基于 django-fsm 修改',
    'long_description': '# Django friendly finite state machine support\n\ndjango-fsm-ex 基于 [django-fsm](https://github.com/kmmbvnr/django-fsm). 不过由于 django-fsm 基本停止开发了,\n本项目在原项目的基础上调整结构,去掉了部分兼容代码.\n调整了结构,增加了类型信息, 优化了错误信息(主要针对中文项目)\n',
    'author': 'codetalks',
    'author_email': 'banxi1988@gmail.com',
    'url': 'https://github.com/banxi1988/django-fsm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
