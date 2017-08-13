Linux
=====

See also : \*
https://cloudmesh.github.io/classes/lesson/linux/linux.html \*
http://www.cs.jhu.edu/~joanne/unixRC.pdf

While using the computer we will interface with many programs form a
terminal that allows us to specify comands in a commandline. We list
here a number of useful commands.

File commands
-------------

+-------------------+-------------------------------------+
| Command           | Description                         |
+===================+=====================================+
| ls                | Directory listing                   |
+-------------------+-------------------------------------+
| ls -lisa          | list details                        |
+-------------------+-------------------------------------+
| cd *dirname*      | Change directory to *dirname*       |
+-------------------+-------------------------------------+
| mkdir *dirname*   | create the directory                |
+-------------------+-------------------------------------+
| pwd               | print working directory             |
+-------------------+-------------------------------------+
| rm *file*         | remove the file                     |
+-------------------+-------------------------------------+
| cp *a* *b*        | copy file *a* to *b*                |
+-------------------+-------------------------------------+
| mv *a* *b*        | move/rename file *a* to *b*         |
+-------------------+-------------------------------------+
| cat *a*           | print content of file\_a\_          |
+-------------------+-------------------------------------+
| less *a*          | print paged content of file *a*     |
+-------------------+-------------------------------------+
| head -5 *a*       | Display first 5 lines of file *a*   |
+-------------------+-------------------------------------+
| tail -5 *a*       | Display last 5 lines of file *a*    |
+-------------------+-------------------------------------+

Search commands
---------------

+------------------------+---------------+
| Command                | Description   |
+========================+===============+
| fgrep                  | TBD           |
+------------------------+---------------+
| grep -R "xyz" .        | TBD           |
+------------------------+---------------+
| find . -name "\*.py"   | TBD           |
+------------------------+---------------+

Help
----

+-----------------+---------------------------------+
| Command         | Description                     |
+=================+=================================+
| man *command*   | manual page for the *command*   |
+-----------------+---------------------------------+

Keyboard Shortcuts
------------------

+------------+----------------------------------------------------------+
| Keys       | Description                                              |
+============+==========================================================+
| Up Arrow   | Show the previous command                                |
+------------+----------------------------------------------------------+
| Ctrl + Z   | Stops the current command                                |
+------------+----------------------------------------------------------+
|            | resume with fg in the foreground                         |
+------------+----------------------------------------------------------+
|            | resume with bg in the background                         |
+------------+----------------------------------------------------------+
| Ctrl + C   | Halts the current command                                |
+------------+----------------------------------------------------------+
| Ctrl + L   | Clear the screen                                         |
+------------+----------------------------------------------------------+
| Ctrl + A   | Return to the start of the command you're typing         |
+------------+----------------------------------------------------------+
| Ctrl + E   | Go to the end of the command you're typing               |
+------------+----------------------------------------------------------+
| Ctrl + K   | Cut everything after the cursor to a special clipboard   |
+------------+----------------------------------------------------------+
| Ctrl + Y   | Paste from the special clipboard                         |
+------------+----------------------------------------------------------+
| Ctrl + D   | Log out of current session, similar to exit              |
+------------+----------------------------------------------------------+

Assignments
-----------

1. Familiarize yourself with the commands
2. Find more commands that you find useful and add them to this page.
