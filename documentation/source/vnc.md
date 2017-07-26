
# Dexter

**Note:** *If you like to connect to your Raspberry from your laptop, we recommend to use VNC. If you rather like to connect a monitor and keyboard as well as a mouse to the RAspberry, you can sckip the steps with the VNC update.*

## Creating an SD Card

### OSX

First, nstall Etcher from  [etcher.io](https://etcher.io/) which allows you to flash images onto the SD card. When flashing make sure you only attach one USB SD card reader/wroiter or use the build in SD card slot provided in some Mac's.

The version of etcher we used is 

* [Etcher-1.1.1-darwin-x64.dmg](https://github.com/resin-io/etcher/releases/download/v1.1.1/Etcher-1.1.1-darwin-x64.dmg) 

Make sure to check if there is a newer version

### Dexter Rasbian


Dexter provides a special image that contains the drivers and sample programs for the GrovePi shield. We hadsome issues installing it on a plain Raspberian OS, thus we recoomend that you use dexters version if you use the GrovePi shield. It is available from 

* [Google Drive](http://sourceforge.net/projects/dexterindustriesraspbianflavor/)
* [Sourceforge](http://sourceforge.net/projects/dexterindustriesraspbianflavor/)



Detailed information on how to generate an SD card while using your OS is provided at 

* [https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/](https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/)

### Github

Dexter mainyains a github repository that includes their code for the shield and many other projects at

* [https://github.com/DexterInd](https://github.com/DexterInd)

## Setting up VNC

We had some issues with the installed version of VNC that is customized for connecting a Laptop via the ethernet cable to the PI. However as we connect wirelessly, our setup is slightly diffrent. The easiset way that we found is to update the Raspbian OS as follows. In a terminal type


	sudo apt-get update
	sudo apt-get install realvnc-vnc-server 
	sudo apt-get install realvnc-vnc-viewer

Next you enable the VNC server in the configuration panel via the Rasbian GUI by selecting

	 Menu > 
	    Preferences > 
	       Raspberry Pi Configuration > 
	          Interfaces.

Here you toggle the VNC service to enabled. As we are already at it in our setup we enabled all other services, especially those that deal with Grove sensor related bins and wires.

Next reboot and double check if the settings are preseved after the reboot

### Install VNC on OSX



To install a vnc server of your liking on your Mac. You find one at

* [http://www.realvnc.com/download/vnc/latest/](http://www.realvnc.com/download/vnc/latest/])

Be sure to download the version of the VNC Viewer for the computer you are going to use to virtually control the Pi (there is a version listed for Raspberry Pi– don’t download this one. For us thi sis the Mac version.)

### Run VNC Viewer on OSX

Once you have downloaded the VNC viewer installed it you can open the program. Next you can start vnc viewer and enter the ip address of your raspberry. Make sure you are on the same network. You can find the address by using ifconfig. 

## Dexter Sample programs

Dexter maintains all GrovePi related programs at

* [https://github.com/DexterInd/GrovePi](https://github.com/DexterInd/GrovePi)

The python related programs are in a sudirectory at

* [https://github.com/DexterInd/GrovePi/tree/master/Software/Python](https://github.com/DexterInd/GrovePi/tree/master/Software/Python)

Here you find many programs and for a complete list visit that link. Dependent on the sensors and actuators you have, inspect some programs. Some of them may inspire you to purchase some sensors. 

A partial list includes progrms for 
	
TBD

## Cloning Grove PI

To clone the GrovePI library on orther computers you can use the command

	git clone https://github.com/DexterInd/GrovePi.git
	
