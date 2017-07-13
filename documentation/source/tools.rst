Tools
=====

Terminal
--------

On OSX, navigate to your *Applications Folder* in *Finder* and open
*Utilities*. In utilities, you will find the *Terminal* application.
Open it and you will be presented with a white text box. You now know
how to navigate to Terminal.

*Terminal* gives you an interface to OS X's bash shell, allowing you to
run programs on your OSX device. In order to run *programs* on OSX,
after typing each *command*, you need to press the *return* button on
your keyboard, in order to make terminal *execute* the command.

Pyenev
------

Python is a tool that allows you to manage Python versions on your
divice. Pyenv lets you change your python version and also allows you to
use commands from multiple python versions. Now we will install Pyenv.
Since you should already have Homebrew installed, installing Pyenv is
very easy. Simply type ``brew install pyenv`` into Terminal, and you
should no be able to use pyenv. to upgrade pyenv in the future, simply
switch the word "install" with "upgrade" in the aforementioned command.

see `README <../README.md>`__

Instalation of tools
--------------------

Once you have installed cloudmesh robots you well be able to install a
numebr of tools automatically with the command

::

    $ cms robot osx install

This will install for you

1. xcode
2. homebrew
3. macdown
4. aquaemacs

If you do not like this automatic install or you have a differnt
operating system, please find alternatives. Let us know how you
installed the tools on Linux or Windows and we will integrate it here.

Xcode
-----

Xcode is an integrated development environment for macOS containing a
suite of software development tools developed by Apple for developing
software for macOS, iOS, watchOS and tvOS.

Homebrew
--------

*Homebrew* is a *package manager* for OS X which lets the user *install
software* from *UNIX* and *open source software* that is not included in
OSX.

Markdown
--------

Markdown has very good support for editors that render the final output
in a view window next to the editor pane. Two such editors are

-  `Macdown <https://macdown.uranusjr.com/>`__: MacDown provides a nice
   integrated editor that works well.
-  `pyCharm <https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC>`__:
   We have successfully used Vladimir Schhneiders `Markdown Navigator
   plugin <https://plugins.jetbrains.com/plugin/7896-markdown-navigator>`__.
   Once installes you click on a .md file pycharm will automatically ask
   to install the plugins from Markdown for you.

Macdown Installation
--------------------

Macdown is an open source editor for *Markdown*.

Is this done with osx install?

In order to install it, you need to navigate to
`Macdown <https://macdown.uranusjr.com/>`__, and click on the "Download
MacDown" button under "What's in the Box?". You may be asked to grant
permission for the file to be installed. Once the program is finished
downloading, navigate to the "downloads" folder in Finder and click on
the MacDown program and you are good to go.

**BUG: I DO NOT THINK THI IS RIGHT.**

Markdown Syntax
~~~~~~~~~~~~~~~

MarkDown is a format convention that produces nicely formated text with
simple ASCII text.

**BUG: LINK TO MARKDOWN SYNTAX MISSING**

The following are some basic examples

-  To *empazise* a text you use ``*empasize*``
-  To make text **bold** use ``**bold**``
-  To make text ***bold-and-emphasize*** use
   ``***bold-and-emphasize***``
-  To create a hyperlink use ``[Google](https://google.com)`` which will
   result in `Google <https://google.com>`__
-  To include an image use ``![Bracketed Text](link)``

A list can be created by item starting with "\*", a "-", or a "+" or a
number

::

    1. one
    2. two

1. one
2. two

   ::

       * one
       * two

-  one
-  two

If you need to indent items underneath already bulleted items, precede
the indent items with four spaces and they will be nested under the item
above them.

To qoute textc precede it with a ">".

::

    > Quote

    Quote

Other syntax options can be found in the Format drop-down at the top of
the screen between View and Plug-ins of macdown.

PyCharm
-------

| PyCharm is an Integrated Development Environment for Python.
| ## AquaEmacs Installation

*Aquamacs* is a program for Mac devices which allows the user to edit
text, HTML, LaTeX, C++, Java, Python, R, Perl, Ruby, PHP, and more.
Aquaemacs integrates well with OSX and provides many functions through a
menu. You will mostly be using the File, Edit, menus or toolbar icons.

Emacs convenient keyboard shortcuts, most of which are combinations with
the Control or Meta key (The Meta key is the ESC key). If you
accidentally end up doing something wrong simply press ``CTRL-g`` to get
out without issue. Other Keyboard Shortcuts include:

-  ``CTRL-x u`` or File>Undo will cancel any command that you did not
   want done. (CHECK)
-  ``ESC-g`` will cancel any command you are in the middle of.
-  You can break paragraph lines with ``Ctrl-x w``, where ``w`` will
   wrap text around word boundaries.

-  To delete text to the end of the current word, press ``ESC-d``.
-  to delete the whole line from the position of the cursor to the end,
   press ``CTRL-k``.

Bash
----

Bash is automatically installed in OSX. A *bash* script contains
*commands* in plain text. In order to create a bash script please decide
for a convenient name. Ltes assume we name our script *myscript*. Than
you can create and edit such a script with

::

    $ touch myscript.sh
    $ emacs myscripts.sh

Next you need to add the following line to the top ogf the script:

::

    !# /bin/bash

To demonstrate how to continue writing a script we will be using the
bash ``echo`` command that allows you to print text. Lets make the
second line

::

    echo "Hello World"

You can now save and start executing your script. Click "File" and then
"Save". Open Terminal and type in ``cd`` followed by the name of the
folder you put the document in. Now we need to execute the script.

*Executing* a Bash script is rather easy. In order to execute a script,
we need to first execute the *permission set*. In order to give Terminal
permission to read/execute a Bash script, you have to type

::

    chmod u+x myscript.sh

After the script has been granted permission to be executed, you can
test it by typing

::

    ./myscript.sh

into the terminal. You will see it prints

::

    Hello World

Optional: Arduino
-----------------

In the event that there is a TTY error, you will need to install
Arduino, since your Mac may be missing some drivers that are included in
Arduino. Simply go to
`Arduino <https://www.arduino.cc/en/guide/macOSX>`__ and click on the
*download page* link under *Download the Arduino Software (IDE)*. You
should be brought to a page with installation options for different OS.
Click on *Mac OS X Lion or Newer* and you should be brought to a
contribution page. You don't have to pay for Arduino, so if you do not
want to contribute, click on *Just Download* and a zip file should be
downloaded. Go to your downloads, uncompress the file, and Arduino
should be in the new directory that is created. Do the one time setup,
and you are finished.

**BUG: IS THIS RIGHT? THIS SEEMS WRONG**

Emacs on OSX
------------

There are many different versions of emacs available on OSX. Aquaemacs
is often used as it integrates nicely with the OSX GUI interface.

-  `AquaEmacs <http://aquamacs.org/download.shtml>`__

Matplotlib on OSX
-----------------

As we typically install python with virtualenv, we need to configure
matplotlib properly to use it. The easiest way to do this is to execute
the following commands. After you run them you can use matplotlib.

::

    $ pip install numpy
    $ pip install matplotlib
    $ echo "backend : TkAgg" > ~/.matplotlib/matplotlibrc

External Tutorials and Lessons
------------------------------

This document leverages a number of lessons created for cloudmesh and
other information. We provide links to these lessons in case you like to
compare or want to learn more about cloudmesh. In particular we
leveraged:

-  `XCode <https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx>`__
   (from cloudmesh)
-  `Pyenv <https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx>`__
   (from cloudmesh)
-  `Pyenv <https://github.com/pyenv/pyenv#how-it-works>`__ (from pyenv)
-  `Homebrew <https://brew.sh>`__ (from homebrew)
-  `Markdown <https://blog.ghost.org/markdown/>`__ (from Markdown)
-  `AquaEmacs <http://oracc.museum.upenn.edu/doc/help/usingemacs/aquamacs/>`__
   (from Aquaemacs)
-  `Marvelmind <http://marvelmind.com/>`__ (from Marvelmind if you have
   marvelmind positioning sensors which are optional)
-  `Arduino <https://www.arduino.cc/en/guide/macOSX>`__ (from Arduino if
   you like to use their interface to access teh esp8266 boards)
-  `40 OSX Terminal
   Tricks <https://computers.tutsplus.com/tutorials/40-terminal-tips-and-tricks-you-never-thought-you-needed--mac-51192>`__
-  `Bash <https://linuxconfig.org/bash-scripting-tutorial>`__
