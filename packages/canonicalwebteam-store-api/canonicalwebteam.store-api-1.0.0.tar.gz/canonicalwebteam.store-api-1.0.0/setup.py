# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['canonicalwebteam',
 'canonicalwebteam.store_api',
 'canonicalwebteam.store_api.stores']

package_data = \
{'': ['*']}

install_requires = \
['pybreaker>=0.6.0,<0.7.0', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'canonicalwebteam.store-api',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Canonical Store Api - Python package\n\n## How to install\n\nTo install this extension as a requirement in your project, you can use PIP:\n\n```bash\npip install canonicalwebteam.store-api\n```\n\nSee also the documentation for [pip install](https://pip.pypa.io/en/stable/reference/pip_install/).\n\n## Development\n\nThe package leverages [poetry](https://poetry.eustace.io/) for dependency management.\n\n## Testing\n\nAll tests can be run with `poetry run pytest`.\n',
    'author': 'Canonical Web Team',
    'author_email': 'webteam@canonical.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
