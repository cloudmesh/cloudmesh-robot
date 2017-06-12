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