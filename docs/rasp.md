# SD Card

## Download Noobs

https://www.raspberrypi.org/downloads/noobs/

Takes >26 min

## Format SD card with Disk Utility

https://www.raspberrypi.org/learning/noobs-install/elcapitan/

MS-DOS (FAT) 

## Copy FIles

Drag all files from the NOOBS folder onto the sd card


## Connecting

Hostnames:

* raspberrypi.local 
* raspberrypi.

change

recovery.cmdline



	runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline
	silentinstall runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline
	

Connect the cable
	
You will see the activity LEDs flash while the OS installs.  Depending on your SD-Card this can take up to 40-60 minutes.

## Update

	sudo apt-get upgrade
	sudo apt-get update
	sudo apt-get install emacs

	curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
	
add to ~/.bash_profile	
	
	export PATH="/home/pi/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"

source 


## VLC on OSX

* [https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)
* [http://www.videolan.org/vlc/index.en_GB.html](http://www.videolan.org/vlc/index.en_GB.html)
* [http://get.videolan.org/vlc/2.2.6/macosx/vlc-2.2.6.dmg](http://get.videolan.org/vlc/2.2.6/macosx/vlc-2.2.6.dmg)
* [http://www.mybigideas.co.uk/RPi/RPiCamera/](http://www.mybigideas.co.uk/RPi/RPiCamera/)
* 
## Camera on Pi

	sudo apt-get install vlc

* [https://www.hackster.io/bestd25/pi-car-016e66](https://www.hackster.io/bestd25/pi-car-016e66)

## STreaming video

* [https://blog.miguelgrinberg.com/post/stream-video-from-the-raspberry-pi-camera-to-web-browsers-even-on-ios-and-android](https://blog.miguelgrinberg.com/post/stream-video-from-the-raspberry-pi-camera-to-web-browsers-even-on-ios-and-android)

# Linux commandline

* [http://www.computerworld.com/article/2598082/linux/linux-linux-command-line-cheat-sheet.html](http://www.computerworld.com/article/2598082/linux/linux-linux-command-line-cheat-sheet.html)



# Setup

	mkdir github
  	cd github
  	git clone https://github.com/cloudmesh/cloudmesh.robot.git
  	ssh-keygen
  	sudo apt-get install emacs
  	git config --global user.name "Gregor von Laszewski"
  	git config --global user.email laszewski@gmail.com
  	git config --global core.editor emacs

# Enable SPI

go to the configuration interfaces and enable
   
# RTIMUlib2

  git clone https://github.com/RTIMULib/RTIMULib2.git
  cd RTIMULib

Add the following two lines to /etc/modules

	i2c-bcm2708
	i2c-dev
