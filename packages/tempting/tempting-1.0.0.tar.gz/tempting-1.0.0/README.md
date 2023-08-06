[![PyPI status](https://img.shields.io/pypi/status/tempting.svg)](https://pypi.python.org/pypi/tempting/)
[![PyPI version](https://img.shields.io/pypi/v/tempting.svg)](https://pypi.python.org/pypi/tempting/)
[![Pipeline status](https://gitlab.com/frkl/tempting/badges/develop/pipeline.svg)](https://gitlab.com/frkl/tempting/pipelines)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# tempting

*Do useful and somewhat weird things with templates.*


## Description

Documentation still to be done.

# Development

Assuming you use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for development, here's how to setup a 'tempting' development environment manually:

    pyenv install 3.7.3
    pyenv virtualenv 3.7.3 tempting
    git clone https://gitlab.com/frkl/tempting
    cd <tempting_dir>
    pyenv local tempting
    pip install -e .[develop,testing,docs]
    pre-commit install
    python setup.py download    # to download default set of temptings

## Copyright & license

[Parity Public License 6.0.0](https://licensezero.com/licenses/parity)


Please check the [LICENSE](/LICENSE) file in this repository (it's a short license!), also check out the [*freckles* license page](https://freckles.io/license) for more details.

### frkl product ids

Versions:

  - 0.9:
    - 97de2bf5-0fbb-4884-9d26-488217e1477c
  - 1.x.x:  
    - 97de2bf5-0fbb-4884-9d26-488217e1477c

[Copyright (c) 2019 frkl OÜ](https://frkl.io)
