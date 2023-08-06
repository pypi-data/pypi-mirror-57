# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fn_graph']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.13.2,<0.14.0', 'littleutils>=0.2.1,<0.3.0', 'networkx>=2.4,<3.0']

setup_kwargs = {
    'name': 'fn-graph',
    'version': '0.1.0',
    'description': 'Manage, maintain and reuse complex function graphs without the hassle.',
    'long_description': None,
    'author': 'James Saunders',
    'author_email': 'james@businessoptics.biz',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
