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
    'version': '0.2.2',
    'description': 'Various formats used in pulsar signal processing',
    'long_description': '### psr-formats\n\nFormats for loading and saving data used in pulsar data processing.\n\nSupported formats:\n  - DADA\n\n### Usage\n\n```python\n>>> from psr_formats import DADAFile\n>>> dada_file = DADAFile("path/to/dada.dump").load_data()\n>>> dada_file["NCHAN"]\n\'1\'\n>>> dada_file.nchan\n1\n>>> dada_file.npol\n2\n>>> dada_file.sampling_rate\n<Quantity 0.025 us>\n>>> dada_file.data.shape\n(3107730, 1, 2) # ndat, nchan, npol\n>>> new_dada_file = DADAFile("new.dump")\n>>> new_dada_file.data = dada_file.data\n>>> new_dada_file.dump_data()\n\'new.dump\'\n```\n\n### Testing\n\n```\npoetry run python -m unittest\n```\n',
    'author': 'Dean Shaff',
    'author_email': 'dshaff@swin.edu.au',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
