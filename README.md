# flaskblog

### python

### To Setup python3 environment follow below steps
	Install virtualenv
	Install virtualenvwrapper
	Edit .bashrc
### Create your virtual environment directory where your all environments will be there
	mkdir .virtualenv

### Install below pacakges 
		sudo apt install python3-pip
		pip3 install virtualenv
		pip3 install virtualenvwrapper

### Open bashrc file.

	vim .bashrc

### update below line in the bashrc file.

	#Virtualenvwrapper settings:
	export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
	export WORKON_HOME=$HOME/.virtualenvs
	export VIRTUALENVWRAPPER_VIRTUALENV=/home/rups/.local/bin/virtualenv
	source ~/.local/bin/virtualenvwrapper.sh
### Then create virtual environment using below command
	mkvirtualenv test_env
	
