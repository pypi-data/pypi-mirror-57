# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['bakers_registry']

package_data = \
{'': ['*']}

install_requires = \
['conseil', 'jsondiff', 'pytezos>=2.2.1,<3.0.0']

entry_points = \
{'console_scripts': ['bakers = bakers_registry:cli.main']}

setup_kwargs = {
    'name': 'bakers-registry',
    'version': '0.1.1',
    'description': 'Command line interface for the Tezos Bakers Registry',
    'long_description': '# Bakers Registry client\n\n[![PyPI version](https://badge.fury.io/py/bakers-registry.svg?)](https://badge.fury.io/py/bakers-registry)\n[![made_with pytezos](https://img.shields.io/badge/made_with-pytezos-brightgreen.svg)](https://github.com/baking-bad/pytezos)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\nConsole client for the [Tezos Bakers Registry](https://tezit.github.io/baker-registry)\n\n## Installation\n\n```bash\npip install bakers-registry\n```\n\n## Usage\n\n### `bakers get` Get a particular baker\n\n### `bakers set` Generate cmdline for `tezos-client`\n\n### `bakers new` Create default config\n\n### `bakers all` Get all bakers\n\n### `bakers log` Get recent changes',
    'author': 'Michael Zaikin',
    'author_email': 'mz@baking-bad.org',
    'url': 'https://github.com/baking-bad/bakers-registry-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
