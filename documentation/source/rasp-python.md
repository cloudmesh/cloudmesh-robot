# Raspberry Pi Python

change python version
-----

* [https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux]  (https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)

Upgrade setuptools for pip install with 

	$ pip3 install --upgrade setuptools
	

Test your python version with

	$ python --version
	
Check your python version alternatives
   
	$ update-alternatives --list python
	
If python2.7 is not in your alternatives, add it with 

	$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
	
If python3.4 is not in your alternatives, add it with 

	$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 2
	
Now make python3.4 to your default with

	update-alternatives --config python
Select python3.4

	

-----
follow steps 1 and 2

* [better get 3.6.1](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f)

-----
pip install cloudmesh.pi
----

pip install cloudmesh.pi with
	
	$ git clone https://github.com/cloudmesh/cloudmesh.pi.git
	$ cd cloudmesh.pi
	$ sudo pip3 install .
with cloudmesh.pi installed, you have access to the GrovePi classes.

