#!/bin/bash

curl  https://pyenv.run | bash

pyenv install 2.7.0
pyenv virtualenv 2.7.0 python2
pyenv install 3.7.0
pyenv virtualenv 3.7.0 python3

