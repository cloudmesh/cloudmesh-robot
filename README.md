# ESP8266

When working with a external hardware such as the nodeMCU you will find a lot of information on the internet about it. It is a bit difficult at times to assess what you need to program it. You are exposed to many choices. A NodeMcu typically comes with Lua. However you have many other choices.
Such choices include multiple programming languages such as Lua, MicroPython, Arduino/C, Go and others.

As all of them are slightly different you need to identify which works best for you. In addition you need to install programs, images and libraries that support your specific language choice.
 
For our first experiments we will be using MicroPython. This choce is motivated by the fact that Python is a well established and easy to learn programming language. Many other programs can be conducted in Python. Rescently many educational istitutions are offering Python as an introductory programming language.  
 
To simplify the setup and use of the esp8266 for MicroPython we developed an easy to use commandline tool that allows users to set up their machine and interact more easily with it. We believe that the interface is so simple that it can also be used in STEM activities and not just in the university or by advanced hobbyists.

## Notation

In this document the `$`  character at a beginning of a command block is used to indicate the terminal prompt. 
When executing the command do not copy it.

## Steup

First we must install a number of tools on the machine connecting to the board.

### OSX

In our guide we will focus on OSX, however, there should not be any issues with modifying our instalations to work with other operating systems, such as Linux or even Windows. If you have improvements in regards to our code, please let us know.

On OSX we will be using homebrew and pyenv to leverage existing libraries and to allow the use of a user managed Python envireonment.

#### Homebrew

Homebrew is a program and package manager that makes it easy to unstall
precompiled programs on your computer.

To install it you need to open a terminal and run the following command

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Install pyenv

Next we install a program called pyenv that will help us managing multiple
versions of python. This is done with the commands

    $ brew update
    $ brew install pyenv
    $ brew install pyenv-virtualenv

#### Install Aquaemacs

You will need an editor to make some modifications to files and write programs. Certainly you can use `vi` or `emacs`. As we are on OSX we can also use an editor such as `aquaemacs`. Let us assume you have installed it on your computer, we recommend to add a shortcut so you can call it from the commandline. This can be done by editing the `~/.bash_profile` and add the following to it:

open_emacs() {
    # open -na Aquamacs $*
    open -a Aquamacs $*    
}

alias emacs=open_emacs

Once done you can start the editor while using the command

	emacs FILENAME
	
where FILENAME is the name of the file you like to edit.


#### Install python 3.6.1

As we want to develop our programs in python we will install it with pyenve as follows

    $ pyenv install 3.6.1
    $ pyenv virtualenv 3.6.1 ENV3

To not forget that you are using python 3 and automatically loading it
we must add it to our `~/.bash_profile` file.

    emacs ~/.bash_profile

Add the following lines at the end of the file

    ######################################################################
    # PYENV
    ######################################################################
    export PYENV_VIRTUALENV_DISABLE_PROMPT=0
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


The above steps have to be done only once

### Instalation of the robot Interafce

To more easily interface with the robot we have developed a convenient
program that is isnatlled as part of a command tool called cloudmesh.



#### Install Cloudmesh Robot 

To install the robot command you simply type

	pip install cloudmesh.robot

This will install a program `cms` on your computer that allows you to
easily communicate with the robot. To test out if the command has been
installed please type

    cms robot welcome
    
If everything works you should see an ASCII image of R2D2 and
C3PO. Next, we still have to install some additional programs before
you can use other commands. This is done with

	cms robot osx install

Once you have successfully installed the commands you can look at the
manaual page of the robot command with

    cms help robot

You will see a manual page like this

    Usage:
        robot welcome
        robot osx install
        robot image fetch
        robot probe [--format=FORMAT]
        robot flash erase [--dryrun]
        robot flash python [--dryrun]
        robot set PORT
        robot put PATH
        robot get PATH
        robot rm PATH
        robot rmdir PATH
        robot ls PATH


### Testing the board

Before we do anything else with the board we test it out first. Once you have plugged it in, 
you can execute the command 

    $ cms robot probe

The output of this command provides you hopefully with a table similar to 
   
    +-----------+---------------------------+
    | Attribute | Value                     |
    +-----------+---------------------------+
    | chipid    | b' 0x00d0f9ec'            |
    | mac       | b' 5c:cf:7f:d0:f9:ec'     |
    | tty       | /dev/tty.wchusbserial1410 |
    +-----------+---------------------------+

Please note that you should only have one board attached to your computer.

### Flashing the image onto the robot board

Next we need to flash the image on the robot board. Naturally we need
to fetch the image first from the internet. We do this with the
command

    robot image fetch
    
This will fetch an image that contains MicroPython into your local
directory.

Next we need to *flash* the imabe on the board. Your board will look
something like this
    
![alt text](images/Official-font-b-DOIT-b-font-ESP-32-ESP-32S-ESP-32-Development-Board-font-b.jpg)

You will need to connect your board to your computer with a USB
cable. The board has a microusb cable adapter.  Make sure to obtain
one as it may not come with the robot.  The board may come with a
preinstalled image such as Lua or some custom image from the
vendor. As we try to program the robot in python let us place
micropython on the board. This requires a number of steps.

#### Erase the chip 

First we need to erase the chip. To follow our instructions place the
chip towrds you as shown in the figure. E.g. the USB connector points
to you.

You must allow the chip to be erased by holding both buttons on the
chip and than letting the right button be released first and than the
left button. YOu will see a blue LED flashing once.  Now you can flash
the chip with the command

    $ cms robot flash erase

#### Putting Python on the chip

To put python on the chip you need to again prepare the board for
flashing while pressing both buttons and releasing the right button
before releasing the left button.

Now ou can place python with the command 

    $ cms robot flash python 
    

#### Testing if it works


To test running a pyton program execute

    $ cms robot test
    
Be careful as it overwrites the file `test.py`.

#### Execute an arbitrary progarm

Lets assume you have placed a progarnm in the file `prg.py` than you can 
run it with the following command

    $ cms robot run prg.py

#### INteractive Python shell on the board

To get into the interactive python shell on the board you need to make sure that you have 
reset the esp8266 once after flashing. You need to press the reset button.

Than you can use the following command to login

    $ cms robot login
    
    




## Development

To contribute to the code and develop new commands we recommend the following setup

	git clone https://github.com/cloudmesch/cloudmesh.common
	git clone https://github.com/cloudmesch/cloudmesh.cmd5
	git clone https://github.com/cloudmesch/cloudmesh.robot
	cd cloudmesh.robot
	make source

### Tools

Markdown has very good support for editors that render the final
output in a view windo next to the editor pane.  Two such editors are

* Macdown: MacDown provides a nice integrated editor that works well.
* pyCharm: We have successfully used Vladimir Schhneiders plugin. When
  you click on a .md file pycharm will automatically ask to install the
  plugins from Markdown for you.



# NOT YET INTEGRATED



Linux
-----

	pip install esptool 
	pip install pyserial 
	pip install adafruit-ampy 
	install lua 
	install picocom

Miniterm
--------

	python -m serial.tools.miniterm -h

<http://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm>

Picocom
-------

	picocom /dev/tty.wchusbserial1410 -b115200 ./probe.py

Ampy
----

	ampy -p /dev/tty.wchusbserial1410 -b115200 run test.py

<https://drive.google.com/file/d/0BwAgplGeEjGPTnB5UXJnMzRMemc/view>

```
usage: esptool.py [-h] [--port PORT] [--baud BAUD]
                  {load_ram,dump_mem,read_mem,write_mem,write_flash,run,
                  image_info,make_image,elf2image,read_mac,chip_id,flash_id,
                  read_flash,verify_flash,erase_flash,version}
                  ...

esptool.py v1.3 - ESP8266 ROM Bootloader Utility

positional arguments:
  {load_ram,dump_mem,read_mem,write_mem,write_flash,run,image_info,
  make_image,elf2image,read_mac,chip_id,flash_id,read_flash,
  verify_flash,erase_flash,version}
                        Run esptool {command} -h for additional help
    load_ram            Download an image to RAM and execute
    dump_mem            Dump arbitrary memory to disk
    read_mem            Read arbitrary memory location
    write_mem           Read-modify-write to arbitrary memory location
    write_flash         Write a binary blob to flash
    run                 Run application code in flash
    image_info          Dump headers from an application image
    make_image          Create an application image from binary files
    elf2image           Create an application image from ELF file
    read_mac            Read MAC address from OTP ROM
    chip_id             Read Chip ID from OTP ROM
    flash_id            Read SPI flash manufacturer and device ID
    read_flash          Read SPI flash content
    verify_flash        Verify a binary blob against flash
    erase_flash         Perform Chip Erase on SPI flash
    version             Print esptool version

optional arguments:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  Serial port device
  --baud BAUD, -b BAUD  Serial port baud rate used when flashing/reading
```  

Robot Commands
--------------

To simplofy interaction with the esp8266 we have written a `robot`
command that allows easy access to files and probe the esp via a USB
port.

	$ cms help robot 
	
	 Usage:
        robot osx install
        robot probe [--format=FORMAT]
        robot set PORT
        robot put PATH
        robot get PATH
        robot rm PATH
        robot rmdir PATH
        robot ls PATH

	  This command does some useful things.
	  
 	 Arguments:
         FILE   a file name

	  Options:
         -f      specify the file


TODO: see we have errors, remove leading space, convert to str 

Other commands are not yet tested   
   

Information
-----------

```
esptool.py -p /dev/tty.wchusbserial1440 chip_id
esptool.py -p /dev/tty.wchusbserial1440 read_mac
```
```
cfg.ssid=“DoitWiFi”; cfg.pwd=“12345678”
```
http://192.168.4.1/

	esptool –port /dev/tty.wchusbserial1460 write_flash 0x00000 doit_integer_car_512k_20150701.bin

	esptool –port /dev/tty.wchusbserial1460 write_flash 0x00000 doit_integer_webserver_512k_20150701.bin
	
	esptool –port /dev/tty.wchusbserial1460 erase_flash

	esptool v1.3 Connecting.... Running Cesanta flasher stub... Erasing
flash (this may take a while)... Erase took 10.6 seconds

http://micropython.org/live/

micropython
-----------

Download image from

micropython.org

Flash

```
esptool.py –port /dev/tty.wchusbserial1410 write_flash –flash_size=detect 0 esp8266-20170108-v1.8.7.bin
```

reset the chip
start 

	picocom /dev/tty.wchusbserial1410 -b115200

terminal

	picocom /dev/tty.wchusbserial1410


Run Code
--------

test.py:

	print('Count to 10:')
	for i in range(1,11):
   		print(i)

Running:

	ampy --port /serial/port run test.py

* /serial/port is the path or name of the serial port connected to the MicroPython board.

Copy a file to the board

	ampy --port /serial/port put test.py

Copy a Directory to the board

	ampy --port /serial/port put adafruit_driver

Copy a file or directory from the board

	ampy --port /serial/port get boot.py

| comand | execute                                |
|--------|----------------------------------------|
| mkdir  | ampy --port /serial/port mkdir foo     |
| ls     | ampy --port /serial/port ls            |
| rm     | ampy --port /serial/port rm test.py    |
| rmdir  | ampy --port /serial/port rmdir test    |



Boot see: https://learn.adafruit.com/micropython-basics-load-files-and-run-code/boot-scripts 

Lua
---

	> pin =1 
	> gpio.mode(pin, gpio.OUTPUT) 
	> gpio.write(pin, gpio.HIGH) 
	> gpio.write(pin, gpio.LOW) 	
	> gpio.write(pin, gpio.LOW)
	> gpio.write(pin, gpio.LOW) 
	> pin=2 
	> gpio.mode(pin, gpio.OUTPUT) 
	> gpio.write(pin, gpio.HIGH) 
	> gpio.write(pin, gpio.LOW)

ampy
----

https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

# Resources

login
-----

    picocom v2.2
    
    port is        : /dev/tty.wchusbserial1460
    flowcontrol    : none
    baudrate is    : 115200
    parity is      : none
    databits are   : 8
    stopbits are   : 1
    escape is      : C-a
    local echo is  : no
    noinit is      : no
    noreset is     : no
    nolock is      : no
    send_cmd is    : sz -vv
    receive_cmd is : rz -vv -E
    imap is        : lfcrlf,
    omap is        : 
    emap is        : crcrlf,delbs,
    
    
Links
-----

* http://micropython.org/resources/docs/en/latest/esp8266/esp8266/tutorial/pins.html?highlight=gpio
* https://cdn.hackaday.io/files/8856378895104/user-mannual-for-esp-12e-motor-shield.pdf
* https://smartarduino.gitbooks.io/user-manual-for-wifi-car-by-nodemcu-doitcar-/content/31_code_for_ap_case_on_doitcar.html
* https://blog.squix.org/2015/09/esp8266-nodemcu-motor-shield-review.html
* https://www.losant.com/blog/top-6-esp8266-modules
* 

Jumper
------
* http://www.instructables.com/id/Motorize-IoT-With-ESP8266/
* https://blog.the-jedi.co.uk/2015/11/26/nodemcu-motor-shield-review/

Projects
--------

* https://www.google.com/search?q=esp8266+projects&rlz=1C5CHFA_enUS727US727&oq=esp8266+&aqs=chrome.0.69i59l3j69i61j69i60l2.3594j0j4&sourceid=chrome&ie=UTF-8
* http://randomnerdtutorials.com/getting-started-with-esp8266-wifi-transceiver-review/

Grove
-----

* https://cknodemcu.wordpress.com/2016/04/21/esp8266-grove-kit-arrived/
* https://www.amazon.com/Seeedstudio-Grove-Base-Shield-NodeMCU/dp/B018FNOWFM/ref=pd_lpo_sbs_504_t_0?_encoding=UTF8&psc=1&refRID=PG5ZRRG08AYRA5XYNF5E
* https://www.seeedstudio.com/Grove-Base-Shield-for-NodeMCU-p-2513.html
* https://www.digikey.com/en/maker/blogs/wio-node-grove-esp8266-wifi-module/57ad3656de7a4e8bb1ba5b2c82d4352f
* http://bbs.smartarduino.com/attachment.php?aid=20
* https://solarbotics.com/product/30316/
* https://solarbotics.com/product/30314/
* 