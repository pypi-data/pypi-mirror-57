# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['recap_argument_graph']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.4,<3.0',
 'pendulum>=2.0,<3.0',
 'pygraphviz>=1.5,<2.0',
 'spacy>=2.2,<3.0']

setup_kwargs = {
    'name': 'recap-argument-graph',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Mirko Lenz',
    'author_email': 'info@mirko-lenz.de',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
