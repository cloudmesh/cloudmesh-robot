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
