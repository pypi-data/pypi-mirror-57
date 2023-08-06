# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['psr_formats']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=3.2,<4.0', 'numpy>=1.16,<2.0']

setup_kwargs = {
    'name': 'psr-formats',
    'version': '0.2.1',
    'description': 'Various formats used in pulsar signal processing',
    'long_description': None,
    'author': 'Dean Shaff',
    'author_email': 'dshaff@swin.edu.au',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
