# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['mkdocstrings']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mkdocstrings = mkdocstrings.cli:main'],
 'mkdocs.plugins': ['mkdocstrings = mkdocstrings.plugin:MkdocstringsPlugin']}

setup_kwargs = {
    'name': 'mkdocstrings',
    'version': '0.1.0',
    'description': 'Automatic documentation from docstrings, for mkdocs.',
    'long_description': '# mkdocstrings\n[![pipeline status](https://gitlab.com/pawamoy/mkdocstrings/badges/master/pipeline.svg)](https://gitlab.com/pawamoy/mkdocstrings/pipelines)\n[![coverage report](https://gitlab.com/pawamoy/mkdocstrings/badges/master/coverage.svg)](https://gitlab.com/pawamoy/mkdocstrings/commits/master)\n[![documentation](https://img.shields.io/readthedocs/mkdocstrings.svg?style=flat)](https://mkdocstrings.readthedocs.io/en/latest/index.html)\n[![pypi version](https://img.shields.io/pypi/v/mkdocstrings.svg)](https://pypi.org/project/mkdocstrings/)\n\nAutomatic documentation from docstrings, for mkdocs.\n\nThis plugin is still in alpha status. Here is how it looks with the [mkdocs-material theme](https://squidfunk.github.io/mkdocs-material/) for now:\n\n![screenshot_mkdocstrings](https://user-images.githubusercontent.com/3999221/70753392-f4282d00-1d34-11ea-987c-0e9372227617.png)\n\n## Requirements\nmkdocstrings requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.8\n\n# make it available globally\npyenv global system 3.6.8\n```\n</details>\n\n## Installation\nWith `pip`:\n```bash\npython3.6 -m pip install mkdocstrings\n```\n\nWith [`pipx`](https://github.com/cs01/pipx):\n```bash\npython3.6 -m pip install --user pipx\n\npipx install --python python3.6 mkdocstrings\n```\n\n## Usage\n\n```yaml\n# mkdocs.yml\nplugins:\n  - mkdocstrings\n```\n\n```markdown\n# Reference\n\n::: my_library.my_module.my_class\n```\n',
    'author': 'Timothée Mazzucotelli',
    'author_email': 'pawamoy@pm.me',
    'url': 'https://gitlab.com/pawamoy/mkdocstrings',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
