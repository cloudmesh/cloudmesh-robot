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

Go to [Link](http://marvelmind.com) and scroll down to the *Latest stable SW to download* section and click the link to download the *Dashboard SW v5.16 + Beacon SW v5.51 + Modem SW 5.51*. After installation completes, open the dashboard file in the downloaded folder. If there is a virus warning for the dashboard download, type in the chatbox in the bottom right for help, the Marvelmind team will most likely send you download links to malware free versions of the download. When you are ready to use the dashboard, open the dashboard program file, and plug in the Marvelmind router/modem, turn on the beacons you want to use as stationary, and click freeze on the bottom right of the menu once you have set them up in the positions you want. This will create a field for the portable beacons to move in. Now turn on the beacon(s) you plan to use as portable ones and scroll down to them in the directory at the bottom of the screen. Find the beacons in the directory, and click on them. The menu on the right should change, at the top there is a Hedgehog Mode option. Enable this option and the portable beacon now shows up blue on the map while the rest show up green. You can now move the portable beacon around and it should move on your minimap. 

**Note:** the stationary beacons have to be frozen before you introduce hedgehog beacons.

If the frozen minimap shows up uneven, you may have to reset the beacons at the (0,0) coordinates by pressing the reset button on the side. If this does not work, then you may continue to reset each beacon and it should eventually even out your map.

**Using the python program:**

In order to get coordinates of the beacons from the python program. Unplug the router from the Windows PC after you have frozen your beacons and introduced the hedgehog beacons. Plug it into your mac computer. Run the marvelmind.py program included in the dashboard package that you downloaded by typing
	
	python marvelmind.py
	
into Terminal. The program should start outputting coordinates of the remote beacons. You can now move the remote beacons around and the marvelmind.py program will pick up on the movement, even if the dashboard on the Windows PC says no connection. You can now implement these coordinates into your python programs.

**Assigning point of origin to a stationary beacon:**

While you're setting up your stationary beacons, keep track of what numbers Marvelmind assigns to each beacon. Whichever beacon you choose to be at the point (0,0,Z), Z being whatever the height of each beacon is, enter the number of that beacon into the *starting beacon tritalateration* box on the table on the right side of the dashboard screen. Now Marvelmind will assign said beacon the x and y coodinates of (0,0) and will assign all other beacons coordinates based on their position in relation to this beacon.