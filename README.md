# SEMA Proto

Prototype for a multi-language, automatically translated, secure communication platform.

# Loacal Setup

Pre-requisites: git, python3, python-virtualenv

Follow these steps:

clone the project (will create a directory)

    git clone git@github.com:totobgycs/sema.git

step into the project directory

    cd sema

create a python virtual environment

    virtualenv -p python3 env

activate the python env

    source env/bin/activate

install the dependencies into the virtual environment

    pip install -r requirements.txt

start the development web server

    heroku local web

# Deployment

The demo is hosted on Heroku

https://semaproto.herokuapp.com
