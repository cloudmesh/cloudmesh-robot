# Setup

## OSX Development Setup

In order for us to program robots, we need to install a development environment on our computer. We only need a very small number of tools as all other wiill be installed automatically if you like.
In particular we need the following tools:

* [XCode](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)
* [Homebrew](https://brew.sh)
* [Pyenv](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)

To summarizes the install please install

	xcode-select --install
	usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	brew update
	brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
	brew install readline xz
	pyenv install 3.6.1
	pyenv virtualenv 3.6.1 ENV3
	
To integrate thisin your environment, please add the following to your ~/.bash_profile

	export PYENV_VIRTUALENV_DISABLE_PROMPT=1
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"

	__pyenv_version_ps1() {
  		local ret=$?;
  		output=$(pyenv version-name)
  		if [[ ! -z $output ]]; then
    		echo -n "($output)"
  		fi
  		return $ret;
	}

	PS1="\$(__pyenv_version_ps1) ${PS1}"
	
	alias ENV3="pyenv activate ENV3"
	
	ENV3
	
	
After you have started a new terminal window you will by default activate Python 3. To make sure pip and setup tools are up to date, you can onece call

	pip install pip -U
	pip install setuptools -U

Other tools such as 

* [Macdown](https://macdown.uranusjr.com/)
* [AquaEmacs](http://aquamacs.org/download.shtml)
* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)

Will be automatically installed for you if you like our automated scripts. To use them we need to install the cloudmeshrobot commands. 

In our final version this will be done with (whic is not yet working)

	pip install cloudmesh.robot
	
Developers are however encouraged to work with the source code. THus you will need to first obtain it as follows

	mkdir github
	cd github
	git clone https://github.com/cloudmesh/cloudmesh.common.git
	git clone https://github.com/cloudmesh/cloudmesh.cmd5.git
	git clone https://github.com/cloudmesh/cloudmesh.robot.git
	cd cloudmesh.robot
	make source
	
If things work out you will see something like this:
	
	$ cms help

	Documented commands (type help <topic>):
	========================================
	EOF     clear    echo  info   q     robot  sleep      usb  version
	banner  default  help  pause  quit  shell  stopwatch  var

To install the rest of the tools we recommend you use the following commands.
Note, that you will need sudo previledges for some of the tools.

	cms osx install
	cms osx driver

## External Tutorials

The following links include tutorials or additional material that may be useful for you to learn more about each tool.

* [Pyenv](https://github.com/pyenv/pyenv#how-it-works)
* [Terminal]() < identify new link original one was spam
* [Bash]() < identify new link as previos link was inaproriate
* [Markdown](https://blog.ghost.org/markdown/)
* [Emacs](http://oracc.museum.upenn.edu/doc/help/usingemacs/aquamacs/)
* [Marvelmind](http://marvelmind.com/) 
* [Arduino](https://www.arduino.cc/en/guide/macOSX)
