#!/bin/sh

virtualenv env
source env/bin/activate

python3.9 -m pip install html5lib requests bs4

# exit virtual env: $deactivate