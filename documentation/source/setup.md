# Setup

	mkdir github
  	cd github
  	git clone https://github.com/cloudmesh/cloudmesh.robot.git
  	ssh-keygen
  	sudo apt-get install -y emacs
	sudo apt-get install -y cmake
	sudo apt-get install -y libqt4-dev
  	git config --global user.name "Gregor von Laszewski"
  	git config --global user.email laszewski@gmail.com
  	git config --global core.editor emacs
	git config --global push.default matching

For OSX we have created a

* [setup.sh](https://raw.githubusercontent.com/cloudmesh/cloudmesh.robot/master/bin/osx/setup.sh)

script that allows you to install in a simple way development tools
that you may find useful for the activities reported on in this repository.

 
