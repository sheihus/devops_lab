#!/bin/bash

curl  https://pyenv.run | bash

CONFIG=`realpath ~/.bashrc`
IFS=$'\n'
PYENVRC='pyenv.rc'

for str in $(cat $PYENVRC)
do
  grep -q $str $CONFIG || echo $str >> $CONFIG
done

source $CONFIG

pyenv install 2.7.16
pyenv virtualenv 2.7.16 python2
pyenv install 3.6.8
pyenv virtualenv 3.6.8 python3

#testing python environment
pyenv activate python2
python -V
pyenv activate python3
python -V
pyenv deactivate
