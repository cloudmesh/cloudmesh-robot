# OSX

In order for us to program robots, we need to install certain robot programs

Programs to install:

* [XCode](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)
* [Macdown](https://macdown.uranusjr.com/)
* [AquaEmacs](http://aquamacs.org/download.shtml)
* [Homebrew](https://brew.sh)
* [Pyenv](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)
* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)
* [Arduino](https://www.arduino.cc/en/guide/macOSX)

# Installations

## Xcode

Xcode **is** an integrated development environment for macOS
containing a suite of software development tools developed by Apple
for developing software for macOS, iOS, watchOS and tvOS.
To **install** it, you need to open the **Terminal** app in **Finder**
and **type** the command:

`$ xcode-select --install`

Press enter and allow a **few moments** for Terminal to **install**
the program.

## Macdown

Macdown **is** an open source editor for **Markdown**. In order
to **install** it, you need to navigate to
[MacDown](https://macdown.uranusjr.com/), and click on the "Download
MacDown" button under "What's in the Box?". You may be asked to grant
permission for the file to be installed. Once the program is finished
downloading, navigate to the "downloads" folder in Finder and click on
the MacDown program and you are good to go.

## AquaEmacs

**Aquamacs** is an **emac editor** for Mac devices which allows the
user **to edit** text, HTML, LaTeX, C++, Java, Python, R, Perl, Ruby,
PHP, and more. In order to run Aquamacs, you have to go to
[Aquamacs](http://aquamacs.org/download.shtml) and click on the
topmost link, which should be the newest version of the program. If
the order changes, look for a link title Aquamacs Emacs X.XX (Right
now the version is 3.3). A download should start. Once it's finished
finished installing, you should go to the *Downloads* folder in
Finder, and open the installed file. You are now ready to use
Aquamacs.

## Homebrew

**Homebrew** is a **package manager** for OS X which lets the
user **install software** from **UNIX** and **open source software**
that is not included in OSX.

In order to install Homebrew, open the Terminal app, and type in the
command

	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

and press the return key.

Allow a few moments for Homebrew to install. Now you have access to
Homebrew.

## Pyenv

Python is a tool that allows you to manage Python versions on your
divice. Pyenv lets you change your python version and also allows you
to use commands from multiple python versions. Now we will install
Pyenv. Since you should already have Homebrew installed, installing
Pyenv is very easy. Simply type `brew install pyenv` into Terminal,
and you should no be able to use pyenv. to upgrade pyenv in the
future, simply switch the word "install" with "upgrade" in the
aforementioned command.

## PyCharm

PyCharm is an Integrated Development Environment for Python. In order
to start using PyCharm, go to
[PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) and
download the community version for MacOS. After the program has
downloaded and installed, you may transfer it to your Applications
folder. Otherwise, you are ready to use PyCharm.

## Arduino

In the event that there is a TTY error, you will need to install
Arduino, since your Mac may be missing some drivers that are included
in Arduino. Simply go to
[Arduino](https://www.arduino.cc/en/guide/macOSX) and click on
the *download page* link under *Download the Arduino Software (IDE)*.
You should be brought to a page with installation options for
different OS. Click on *Mac OS X Lion or Newer* and you should be
brought to a contribution page. You don't have to pay for Arduino, so
if you do not want to contribute, click on *Just Download* and a zip
file should be downloaded. Go to your downloads, uncompress the file,
and Arduino should be in the new directory that is created. Do the one
time setup, and you are finished.

# Tutorials

Tutorials we need:

* [Terminal](http://www.imore.com/how-use-terminal-mac-when-you-have-no-idea-where-start)
* [Bash](https://www.hastac.org/blogs/joe-cutajar/2015/04/21/how-make-simple-bash-script-mac)
* [Markdown](https://blog.ghost.org/markdown/)
* [Emacs](http://oracc.museum.upenn.edu/doc/help/usingemacs/aquamacs/)
* [Pyenv](https://github.com/pyenv/pyenv#how-it-works)
* Pycharm (MISSING))
* [Marvelmind](http://marvelmind.com/)

## Terminal

On OSX, navigate to your **Applications Folder** in **Finder** and
open **Utilities**. In utilities, you will find the **Terminal**
application. Open it and you will be presented with a white text box.
You now know how to navigate to Terminal.

**Terminal** gives you an interface to OS X's bash shell, allowing you
to run programs on your OSX device. In order to run **programs** on
OSX, after typing each **command**, you need to press the **return**
button on your keyboard, in order to make terminal **execute** the
command.

## Bash

A *bash* script contains *commands* in plain text. These usually
consist of commands one would typically type into a command line and
also commands we could not normally type into a command line.

In order to start using Bash in Terminal, you must type 

	!/bin/bash

into the white text box. The `echo` command allows you to print the
plain text that follows it, which will allow you to type in Bash
scripts.

You can now save and start executing your script. Click "File" and
then "Save", and uncheck the box that says "if no extension is
provided, use '.txt'." Now Open Finder, find your script file, and
click "Get Info". A window should open. Click the Lock icon that
appears on the bottom right of the window, type in your password to
unlock it.

Open Terminal and type in `cd` followed by the name of the folder you
put the document in. Now we need to execute the script.

**Executing** a Bash script is rather easy. In order to execute a
script, we need to first execute the **permission set**. In order to
give Terminal permission to read/execute a Bash script, you have to
type
	
	chmod a+x sciptname

into **Terminal** (scriptname should be replaced with the name of your
scripts)

After the script has been granted permission to be executed, you can
test it by typing

	./scriptname 

into **Terminal**

If you get an error, then the permission set did not execute. This is
not a big deal. You may execute it again by following the
aforementioned steps.

You can now work with your bash script in **Terminal**.

## MarkDown

MarkDown is a text editing software which allows simple ways to format
text. MarkDown has most of the simple formatting options available in
Word or HTML documents. Here the formatting effects included in
MarkDown:

* If you need to emphasize text, you can wrap it in asterisks.
  Different number of asterisks produce different results:

Text in between two single asterisks becomes *italic*

Text in between two double asterisks becomes **bold**

And text in between two tripple asterisks becomes ***bold-italic***

* In order to hyperlink text, you can wrap them in brackets, and then
  put the link in parenthesis after the bracketed text.

Example:

	[Bracketed Text]+(link)

Type this without the plus sign and you will have a hyperlink.

* Formatting images have the same format as links, preceded by a `!`.

Example: 

	![Bracketed Text]+(link)

Type this without the plus signs and you will have an image and the
bracketed text is now the alt text.

* In order to make lists, you have to:

Make sure each item is preceded by a "*", a "-", or a "+"

This will give you a bulletpoint list.

If you need to indent items underneath already bulleted items, precede
the indent items with four spaces and they will be nested under the
item above them.

For numbered lists, just use numbers instead of bullets, but the
format remains the same.

* To qoute text:

Precede it with a ">".

Example >"Quote" =

	>Quote

Other syntax options can be found in the Format drop-down at the top
of the screen between View and Plug-ins.

Lastly, in order to start a new line of text, you need to press return
twice, instead of once like in word.

##Emacs

Starting out with Aquamacs, you should first set the default font. You
can open and close the Fonts window with the command ⌘⇧T. Pick a font
of your liking and close the Fonts window. The menus provide you with
the basic commands you will be using, and most menus are in spots
typical to most OSX programs.

There is some terminology in Aquamacs that can be confusing. For example:

* A **buffer** is the view of a document.
* **Frames** are windows which may contain more than one **tab**, each
  of which will have a different **buffer** similar to a web browser.
* A **directory** is a folder while **search** is essentially the "find" OSX feature.

You will mostly be using the File, Edit, Options, and Windows menus.

There is a toolbar at the top of each frame of Emacs. This toolbar
consists of icons representing basic file and editing commands. Items
can be added and removed from the toolbar. You can do this by
selecting or deselecting them in the Options> View> Toolbar Items
menu.

Emac also has keyboard shortcuts, most of which are combinations with
the Control or Meta keys.

The minibuffer is Emac's little window that appears at the bottom of a
frame when you type a command. You also type the text you want to find
and replace into the minibuffer. If you accidentally end up in the
minibuffer, you can press Ctrl+g to get out without issue.

While the Ctrl key is the Mac's control key, the Meta key is the esc
key. Therefore, anywhere that you need the Meta key to execute a
command, you should use the esc key.

**Keyboard Shortcuts:**

* File>Undo will cancel any command that you did not want done.
* `Ctrl-x` will cancel any command you are in the middle of.
* You can break paragraph lines with `Ctrl-x W`, where `W` will wrap text around word boundaries.
* To change case, position the cursor at the end of the current word, and press M-u for uppercase, M-l for lower case, and M-c for initial capital.

* To delete text to the end of the current word, press M-d.
* To delete text to the start of the current word, press M-Del. (Del is the normal Delete key)
* to delete the whole line from the position of the cursor to the end, press C-k.

* Transpose two adjacent characters with C-t (for "transpose").
* Transpose two adjacent words with M-t.
* Transpose two adjacent lines with C-x C-t.

* To sort lines in alphabetical order, select them and then press M-x.

##Pyenv

As mentioned in the "Installation" section, Pyenv is a program that
allows you to install and manage different versions of Python
separately, or at once. Here is a list of Pyenv commands that can be
typed into terminal to make changes to your current version(s) of
Python:

`PYENV_VERSION` Specifies the Python version to be used.

`PYENV_ROOT` Defines the directory under which Python versions and shims reside.

`PYENV_DEBUG` Outputs debug information.

`PYENV_HOOK_PATH` Colon-separated list of paths searched for pyenv hooks.

`PYENV_DIR` Directory to start searching for .python-version files.

##Marvelmind

###What is Marvelmind?

Marvelmind Indoor Navigation System is an off-the-shelf indoor navigation system designed for
providing precise (+-2cm) location data to autonomous robots, vehicles (AGV) and copters.

###How to set up the Marvelmind environment.

Go to [Google Docs Link Gregor] and click the link to download the *Dashboard SW v5.16 + Beacon SW v5.51 + Modem SW 5.51* file. After installation completes, open the dashboard file in the downloaded folder. The dashboard interface should give you an error as shown in *Figure 1*.

*Figure 1: Marvelmind error if modem is not plugged in.*

![Figure 1](images/Figure1.png)


The error in *Figure 1* essentially signals that you have not plugged in the Marvelmind modem into your Windows PC yet, which is shown in *Figure 2*. Without this modem, you will not be able to use the Marvelmind dashboard to set up your Marvelmind navigation environment.

*Figure 2: Marvelmind modem.*

![Figure 2](images/Figure2.jpg)

Once the modem is plugged into the Windows PC using a USB cable, with the Marvelmind dashboard running, the error should go away, and you will be presented with a coordinate plane, as demonstrated in *Figure 3*. There should be an error at the top left corner of the coordinate plane stating that not enough beacons are available. This error is due to the fact that you have not turned on enough beacons (minimum of 2) required to track movement with the dashboard environment. You now need to set up stationary and mobile beacons, as needed, to fit your navigational needs.

*Figure 3: Marvelmind coordinate plane.*

![Figure 3](images/Figure3.png)

###How to set up stationary beacons in Marvelmind?

Marvelmind uses stationary beacons in order to track its mobile beacons. Any Marvelmind beacon, *Figure 4*, can be assigned the duty of being stationary or mobile, and it is up to you to decide how many beacons you would like to set up as stationary, or tracker, beacons. The larger the space you operate your environment in, the larger the amount of tracker beacons you should use. Keep in mind, the stationary beacons need to be a good distance apart, 3 meters is a good measure, and their recommended height is at least 1.85 meters. Therefore it is a good idea to mount the stationary beacons on stands of heights equal to or greater than 1.85 meters using velcro tape, as shown in *Figure 5*. 

*Figure 4: Marvelmind beacon.*

![Figure 4](images/Figure4.jpg)

*Figure 5: Stand used to hold Marvelmind stationary beacon in place above recommended height.*

![Figure 5](images/Figure5.jpg)

Now that you have set up your beacons on top of the stands. You may turn them on one by one. The beacons will start showing up on the Marvelmind dashboard, they take approximaely 8 seconds to wake up, as green circles with random device addresses assigned to them, consisting of numbers between 1 and 99, as shown in *Figure 6*. Keep track of the numbers Marvelmind assigns to each beacon, as you can name them to your liking. You can now assign one of the beacons the coordinates (0,0,Z), Z being the height of the beacon, by making it the starting beacon. The menu to the right of the dashboard interface, *Figure 7*, has an option labeled **starting beacon tritalateration**. You can type the device address number of whichever beacon you would like to use as your point (0,0, Z) in terms of the x and y value, respectibly. The other beacons will now remap themselves around this beacon on the dashboard interface.

*Figure 6: Marvelmind beacon list.*

![Figure 6](images/Figure6.png)

*Figure 7: First cell shows starting beacon trilateration.*

At the bottom of your dashboard there is a list of all 99 beacon addresses, as shown in *Figure 8*. Find each beacon the device address number of which you would like to change, and click on it and the menu presented to you on the right side of the dashboard interface should change to look like *Figure 9*. In this new menu, click the **Device address** option and type in whatever number, between 1 and 99, that you would like to assign to this specific beacon, as long as another active beacon does not have it. The beacon should now change device addresses. Do this for as many beacons as you like.

*Figure 8: List of beacons circled red.*

![Figure 8](images/Figure8.png)

*Figure 9: Menu you are presented with once you click a specific beacon to edit its settings.*

![Figure 9](images/Figure9.png)

Now that you have assigned your beacons device addresses to your liking and have picked a starting beacon, you can click the option **freeze map** at the bottom right corner of the coordinate plane, *Figure 10*, and lock your beacons as stationary on the Marvelmind screen. Now you can move on to introducing mobile beacons that will be picked up by these stationary beacons to your environment.

*Figure 10: "Freeze map" option circled red.*

![Figure 10](images/Figure10.png)

###How to set up mobile beacons in Marvelmind?

Once you have frozen the stationary beacons, you can now start introducing mobile beacons to Marvelmind. These mobile beacons can be mounted on whatever object you are trying to measure the movement of using Marvelmind, such as a robot. In order to introduce a beacon as a mobile beacon. Simply turn a beacon, or as many as you would like, on in addition to the frozen beacons, it will show up green just like the other beacons on the dashboard. Find the beacon number in the list shown in *Figure 9* of this newly started beacon, renumber it like demonstrated earlier, or keep the address if that's your preference. Click on the beacon number in the list and the menu on the right should change again, as demonstrated in *Figure 8*. Now, there should be an option at the top of this menu labeled *Hedgehog mode* and it should be **disabled**. Click on it so it says **enabled**. The beacon should now turn blue on the coordinate plane, as shown in *Figure 11*.

*Figure 11: Hedgehog beacon and its setting.*

![Figure 11](images/Figure11.png)

You can now move the beacon around as it is mobile, while the frozen beacons remain stationary. Now the Marvelmind python program, which you will find in the dashboard package that you downloaded from google docs, can be used to track the coordinates of this beacon, essentially tracking whatever object it is mounted on. If you are mounting other objects on top of the device you are tracking in addition to the beacon, you will need holders for mobile beacons that allow the beacons to be mounted higher up than everything else mounted on the device, so that they do not block the sound recepters on the beacons, since that's the stationary beacons' way of receiving feedback from the mobile ones. *Figure 12* shows a selfie stick that can be purchased from any local store that seems to function very well as a holder for the beacons. Just make sure the beacon is not too far into the holder, because the recepters may become blocked off.

*Figure 12: Selfie stick used as a hedgehog beacon holder (note how the sound receptors are elevated above the grip of the beacons).*

![Figure 12](images/Figure12.jpg)

**Using the python program:**

In order to get coordinates of the beacons from the python program. Unplug the modem from the Windows PC after you have frozen your stationary beacons and introduced the mobile beacon(s). Plug it into your mac computer. Navigate to the directory that houses your marvelmind.py program in terminal, which by default is the Marvelmind dashboard folder. Run the marvelmind.py program included in the dashboard package that you downloaded by typing
	
	python marvelmind.py
	
into Terminal. The program should start outputting coordinates of the remote beacons, as shown in *Figure 13*. You can now move the remote beacon(s) around and the marvelmind.py program will pick up on the movement, even if the dashboard on the Windows PC says there is no connection. You can now implement these coordinates into your python programs.

*Figure 13: Marvelmind coordinates presented as units of (X,Y,Z, and time elapsed since the program has been running).*

![Figure 13](images/Figure13.png)