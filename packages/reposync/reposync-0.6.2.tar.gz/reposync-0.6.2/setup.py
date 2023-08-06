# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reposync', 'reposync.console']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0', 'gitpython>=3.0.5,<4.0.0', 'pyaml>=19.12.0,<20.0.0']

entry_points = \
{'console_scripts': ['reposync = reposync.console:main']}

setup_kwargs = {
    'name': 'reposync',
    'version': '0.6.2',
    'description': 'Organize git repositories.',
    'long_description': "# reposync\n\nreposync helps you manage a lot of git repositories. By declaring the repositories in a YAML file, reposync can then apply various git commands (limited to `clone` and `pull` for now) to the repositories in appropriate manners.\n\n## Installation\n\n`$ pip install reposync`\n\n## Usage\n\nDeclare repositories in `repositories.yaml` like so:\n\n```\nProjects:\n  Past:\n    alpha: github.com/yourusername/alpha\n  Current:\n    beta: github.com/yourusername/beta\n    omega: github.com/yourusername/omega\n\nDotfiles: github.com/yourusername/dotfiles\n\nOthers:\n  TensorFlow: github.com/tensorflow/tensorflow\n  Helm: [go, github.com/helm/helm]\n```\n\nThen run `$ reposync clone` to clone the repositories, resulting in the directory structure below:\n\n```\n.\n├── Projects\n│\xa0\xa0 ├── Past\n│\xa0\xa0 │\xa0\xa0 └── alpha\n│\xa0\xa0 └── Current\n│\xa0\xa0  \xa0\xa0 └── beta\n│\xa0\xa0  \xa0\xa0 └── omega\n├── Dotfiles\n└── Others\n \xa0\xa0 ├── TensorFlow\n \xa0\xa0 └── Helm\n```\n\nTo update these repositories, use `$ reposync pull`.\n\nYou can specify the YAML file with `--file <filename>.yaml`. For the full options, see `$ reposync -- --help`.\n\n### Go Support\n\nIn Go, it is preferred to put repositories at GOPATH. reposync supports this by cloning the Go repositories to their proper path in GOPATH (simulating `go get`), then creates symbolic links to the repositories at the path specified.\n\nTo specify a Go repository, you need to put a special list. In the example above, `Helm` is a Go repository and its value is `[go, github.com/helm/helm]`. The first element indicates Go repository, the second is the import path, and the last is the binary location (optional, defaults to the import path).\n\nInternally, reposync will first run `git clone https://github.com/helm/helm $GOPATH/src/github.com/helm/helm` then `ln -s $GOPATH/src/github.com/helm/helm Others/Helm`.\n\n### SSH Support\n\nReposync supports cloning repositories using ssh, just pass `--method=ssh` (which defaults to `--method=https`). This argument will make reposync automatically use repository URLs' (found in `repositories.yaml`) corresponding ssh URLs.\n\n### Concurrency Support\n\nReposync supports executing commands concurrently via multithreading by passing `--concurrent`.\n",
    'author': 'Devin Alvaro',
    'author_email': 'devin.alvaro@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/devinalvaro/reposync',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
