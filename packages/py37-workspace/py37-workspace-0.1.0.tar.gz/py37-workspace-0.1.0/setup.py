# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['py37_workspace']

package_data = \
{'': ['*']}

install_requires = \
['Alfred-Workflow>=1.37,<2.0',
 'ipython>=7.9,<8.0',
 'jupyter>=1.0,<2.0',
 'openpyxl>=3.0,<4.0',
 'pyppeteer>=0.0.25,<0.0.26',
 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'py37-workspace',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
