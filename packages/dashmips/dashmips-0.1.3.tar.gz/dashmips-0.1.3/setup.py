# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dashmips', 'dashmips.instructions', 'dashmips.plugins', 'dashmips.syscalls']

package_data = \
{'': ['*']}

install_requires = \
['websockets>=8.0.2,<9.0.0']

extras_require = \
{':python_version == "3.6"': ['dataclasses>=0.6,<0.7']}

entry_points = \
{'console_scripts': ['dashmips = dashmips.__main__:main']}

setup_kwargs = {
    'name': 'dashmips',
    'version': '0.1.3',
    'description': 'Mips Interpreter',
    'long_description': '# Dashmips\n\n<img src="https://roadkillco.gallerycdn.vsassets.io/extensions/roadkillco/dashmips-debugger/0.1.2/1567790555112/Microsoft.VisualStudio.Services.Icons.Default" height="128" align="right" alt="dashmips icon">\n\n`dashmips` is a Mips Interpreter CLI program.\n\n## [Documentation](https://github.com/nbbeeken/dashmips/wiki)\n\nYou can reference [this repository\'s wiki page](https://github.com/nbbeeken/dashmips/wiki) for CLI usage, debugging, and more!\n\n<sub>Happy coding!</sub>\n',
    'author': 'Neal Beeken',
    'author_email': 'nbbeeken@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nbbeeken/dashmips',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
