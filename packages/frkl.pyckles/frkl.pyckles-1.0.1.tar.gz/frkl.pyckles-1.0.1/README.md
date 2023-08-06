[![PyPI status](https://img.shields.io/pypi/status/pyckles.svg)](https://pypi.python.org/pypi/pyckles/)
[![PyPI version](https://img.shields.io/pypi/v/pyckles.svg)](https://pypi.python.org/pypi/pyckles/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyckles.svg)](https://pypi.python.org/pypi/pyckles/)
[![Pipeline status](https://gitlab.com/frkl/pyckles/badges/develop/pipeline.svg)](https://gitlab.com/frkl/pyckles/pipelines)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# pyckles

*Generate Python code from frecklets.*


## Description

Documentation still to be done.

## Generating Python project

git init
pre-commit install
git add * .*
pre-commit run --all-files
git add * .*



# Development

Assuming you use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for development, here's how to setup a 'pyckles' development environment manually:

    pyenv install 3.7.3
    pyenv virtualenv 3.7.3 pyckles
    git clone https://gitlab.com/frkl/pyckles
    cd <pyckles_dir>
    pyenv local pyckles
    pip install -e .[develop,testing,docs]
    pre-commit install


## Copyright & license

Please check the [LICENSE](/LICENSE) file in this repository (it's a short license!), also check out the [*freckles* license page](https://freckles.io/license) for more details.

[Parity Public License 6.0.0](https://licensezero.com/licenses/parity)

[Copyright (c) 2019 frkl OÜ](https://frkl.io)
