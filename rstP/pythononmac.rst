.. index:: mac
   osx


Some Special Mac Instructions
=============================

While the Python language changes slowly, operating systems and setup methods change 
more rapidly with succeeding versions.  
The attempt here is to keep all such information in one place for the Mac OS-X operating system.
It may become out of date at any time.

I will assume a version of Max OSX of at least High Sierra (10.13 or later).  Upgrades are free.

Versions
---------------

I will use Python 3.7+ to mean the current version of Python, with version number at least
3.7.4.    
Make sure you have the latest recommended version installed from https://www.python.org/downloads/.
Download the pkg file and double click to execute.  


.. _edit-by-default-m:

Editing by Default in Idle
---------------------------

You will be working mostly with files ending in .py -- Python source files.  
Most of the time you will be editing them and running them in IDLE, so the best
default behavior when opening a file with extension .py is to have it open in
Idle 3.7+.  If you can double click on a .py file in my examples, 
and Idle opens as soon as you have installed Python 3.7+, great - you should skip the rest of this section. 

If Idle did not open, here is how to change the default behavior:

#.  In the Finder go to a file in my examples folder with the .py extension.
    and right click or control click on it. Select **Get Info**.
#.  In the Info window that pops up, In the drop-down menu for **Open with:**, 
    you want to see 
    **IDLE.app** on the top line (meaning it is already the default).  
    You may possibly also see the version listed if you have several.  Presumably
    you are going through this because you do *not* see IDLE.app there.  
#.  You may see **IDLE.app** lower down in the list of options.  Then select it there.
#.  If you did not see IDLE.app in the drop-down list at all: 

    *  Select **Other...**.
    *  A window of apps pops up. 
       Toward the bottom is a check box for "Always Open With".  Check it.
    *  If you do not see a Python folder in the list, just below the bottom of
       the page change Recommended Applications to All Applications
    *  Now you should see a Python 3.7 folder.  Open it and select Idle.app.

#.  The Info window should become active again.  Be sure that now under
    **Open with:** you see IDLE.app.
#.  Under the IDLE.app you should see a button, **Change All...**.
    So that you never have to go through all these steps again, be sure to click 
    that button.  A confirmation window will pop up.  Select Continue.
#.  Now you can close the Info window, and you should be able to open all .py 
    files directly in Idle for editing by double clicking in the Finder!
#.  Then if you should happen to want to directly run a Python file from the Finder window,
    you will need to select the file with control-click or right-click 
    and select the latest Python Launcher for Python 3.


.. old
    Setup of Preferences for Launching Python 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    You will sometimes want to run Python programs without Idle.  Assuming you do not
    make this the default behavior, here is how to do it as necessary.
    You use the Python Launcher (for the latest version of Python), 
    but the Python Launcher may need to be configured correctly:

    #.  Type enough of "Python Launcher" into Spotlight so it comes up as a choice.
        If you have several versions of Python install, 
        version numbers will be listed after different versions.  
        Use the latest version.
    #.  A Preferences window pops up for Python scripts.  Set the Interpreter to
        
           /usr/bin/python3

        That may mean just changing the last character from w to 3.  
    #.  Close the Preferences window.  You are set for launch.

    Launching Python Programs Without Idle
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Make sure you have done the previous section's setup first.  Now:

    #.  In the Finder go to the .py file you want (likely in my examples folder)
        and right click or control click on it. Select **Open With**.
    #.  In the window that pops up, select "Python Launcher.app".  
        If there are several, select the latest version.  
        A terminal window should pop up, with your program started.  
    #.  If your program opens a graphics window, 
        it may be all or partly covered by another window, so you may need
        to hunt around and click on its title bar to bring it forward.

   

Running Graphics (Chapter 2)
----------------------------

The graphics window likely comes up behind an unneeded Console Window. You can
close the console window, and click on the graphics window title bar to
bring it to the front.   

Chapter 4 CGI Instructions 
-----------------------------

Opening .cgi Files in Idle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By convention the server programs that you will be writing end in ".cgi".
That is not an extension that is automatically associated with Idle for editing.
You will want to change the association.  Do it the same way as the instructions
above for getting .py files to open in Idle by default, except choose a .cgi file in my www
folder, and go through the same procedure.


Setup: Making CGI Scripts Executable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A complication on a Mac, like any Unix derived system, is that programs
that you run must be explicitly marked *executable*. (On Windows it follows from
the file extension, like .exe.)  The examples/www folder may not
have the cgi files marked executable (nor have several other technical things right).

The example program examples/www/CGIfix.py is used to give direct
Unix/Mac/Linux executability to CGI files for Chapter 4.

In the finder open your www directory. You can open CGIfix.py in Idle and run it. 
Note the comment that the file ``cgiServerScript`` was created.  
This is used to lauch the local server.

Important! Particularly if you later copy in a CGI script from a Windows
machine, or if you *create any new cgi script* in the www directory, make sure
it becomes executable (and possibly fix some other technical things) by 
launching CGIfix.py again.

If you forget this, and the file is not executable,
nothing happens in the browser when you try to run it, 
and the error message in the server window is very unhelpful -
it says  "... File not found ...".  Make sure you make new CGI files
executable (with CGIfix.py)!  Running it extra times does not hurt.

.. old

    ..  warning

      I have been shown an apparent problem copying a partner's script from Windows,
      that I though my CGIfix.py should handle, but it has not.  
      When transferring a cgi file from Windows, you may want to 
      open a new file window and then copy all the contnets in from a separately opened,
      originally Windows 
      file.  Then save the new file and use CGIfix.py.

    There are two setup issues to check, and then general instructions for
    dealing with individual cgi programs.

    Setup: Finding Python3 And Idle3 With a Terminal
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The names python3 and idle3 generally refer to the latest versions 
    that run under Python 3.  You would like these to work in various contexts.

    This section is for testing and fixing where things do not work as expected.

    Open a terminal window (spotlight: Terminal)
       
    Enter

          python3

    If a Python shell starts, fine. Just press Crtl-D once to quit, and you have 
    found python3.   

    Also try

        idle3
        
    **If idle3 or python3 did not start**, you will need to follow these instructions:

    First check the location of the system Python files.  If you have
    Python 3.3, try this terminal command:

       ls /Library/Frameworks/Python.framework/Versions/3.3/bin
       
    If you have Python 3.2, 3.4, ..., replace the 3.3 in the command above.  

    If your command does not cause an error, and shows python3 and idle3 listed, 
    enter the following terminal commands:

       ls /usr/local/bin
     
    If python3 was *not* listed, copy and enter:

       sudo ln -s /Library/Frameworks/Python.framework/Versions/3.3/bin/python3 /usr/local/bin

    You may be asked for your password.  
    *You may get no feedback as you type your password.*

    This should have made python3 accessible.  Now test:  Again try the command

       python3
       
    It should work now. End the command by entering Ctrl-D.

    If python3 still did not work, try a further step: copy and enter:

       sudo ln -s  /usr/local/bin/python3 /usr/bin 

    Now try the python3 command.  If it still did not work, get help.

    If idle3 did not work, enter a similar line:

       sudo ln -s /Library/Frameworks/Python.framework/Versions/3.3/bin/idle3 /usr/local/bin

    Now test, starting idle3 from the command line.

    If that did not work, do the backup:

       sudo ln -s  /usr/local/bin/idle3 /usr/bin 

    If the idle3 command does not work now, get help.


    Idle From a Terminal - Opening CGI Files
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This section assumes you successfully completed the previous section,
    getting python3 and idle3 running from a terminal.

    There is one annoying feature of Idle (and some other programs) on a Mac: 
    The Open File dialog inside 
    Idle only allows you to open files ending in .py or .txt, but not .cgi.  
    Before chapter 4 this is not generally an issue.

    A way to get an existing CGI file into
    Idle:

    *  cd into the folder of the file
    *  enter the command **idle3** *followed by the file name*. 

    For example you could edit and modify adder.cgi if you change to the 
    www
    folder (inside the examples folder) and enter

       idle3 adder.cgi

    Once you have opened a .cgi file this way, Idle should allow you to 
    reopen it later from the Recent Files menu option.

    Setup: Making CGI scripts executable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Make sure you have completed the previous section successfully before 
    going on to this section.

    A complication on a Mac, like any Unix derived system, is that programs
    that you run must be explicitly marked *executable*. (On Windows it follows from
    the file extension, like .exe.)  The examples/www folder may not
    have the cgi files marked executable.

    The example program examples/www/CGIfix.py is needed to give direct
    Unix/Mac/Linux executability to CGI files for Chapter 4 and for any
    Python program in general.

    Remember the www directory cannot have a directory name in the path down to
    that directory with a space in it. If you got that wrong, move your files or
    change the name of the offending folder if possible.

    Change into your www directory. For example if the
    example folder is directly in your desktop folder as in the example
    above, then enter:

        cd ~/desktop/examples/www

    Now make important files executable with the command:

        python3 CGIfix.py CGIfix.py localCGIServer.py

    (Note CGIfix.py is entered twice, once as the Python file to interpret and once
    again as a parameter to that program!)

    Finish with the command:

       ./CGIfix.py

    Do not forget the initial "./".
    This should make all the example cgi scripts executable.

    Running CGI Scripts
    ~~~~~~~~~~~~~~~~~~~~~~

    Important! Particularly if you later copy in a CGI script from a Windows
    machine, or if you *create any new cgi script* in the www directory, make sure
    it becomes executable (and possibly fix some other technical things) by running

       ./CGIfix.py

    from the www directory again. You might want to just
    leave a terminal window open in your www directory. 

    If you forget this, and the file is not executable,
    nothing happens in the browser when you try to run it, 
    and the error message in the server window is very unhelpful -
    it says  "... File not found ...".  Make sure you make new CGI files
    executable!

    If you create and
    edit a cgi file inside Idle, remember you *cannot run it* from inside
    Idle.  After editing, be **sure** to check the syntax, 
    using alt/option-X.
    You should close the file in Idle before running ./CGIfix.py.

    When you want to test a cgi script, you need localCGIServer.py running
    from the www directory.
    Again, assuming for illustration that you put the examples folder on
    your desktop, you could type in the command:

        cd ~/desktop/examples/www
        
    Here is a neat general alternate way to get to a folder in a terminal.  
    The www folder is used as an example:

    * Type ``cd`` and a space and *stop - no return yet*.  
    * Find the www folder in the Finder and drag the www folder to the terminal:  
      The full path should appear in the terminal.
    * Press return to execute the command, and change the directory.

    Once in the www directory enter

        ./localCGIServer.py

    You can just leave the server running. If you want to stop it, you can
    press Ctrl-C, or close its terminal window.  Do not forget the initial "./".

    At this point you can do all the web server based activities in Chapter
    4, with the *only extra step being the running of ./CGIfix.py when you*
    *create a new CGI script* in the www directory, or copy one from Windows.
    There are a number of steps: be sure you carefully go through the list in the tutorial.
    Remember, in your web browser
    with a URL starting with localhost:8080/

    ..  warning

    	I have recently been shown an apparent problem copying scripts from Windows,
    	that I though my CGIfix.py should handle, but it has not.  
    	When transferring a cgi file from Windows, you may want to 
    	open a new file window and then copy the data in from an originally Windows 
    	file.  Then save the new file and use ./CGIfix.py.



Terminal Use (Optional)
----------------------------------

To use the Hands-on Python Tutorial, the information above should be sufficient
to get your Mac usage going.  Terminals are quite useful in other contexts:
There are many things that can be
done from such a window that cannot be done from the Finder or with an App.

If you would like a bit more background, read on.

Navigation
~~~~~~~~~~~~

OS X and Unix (from which OS X is derived) 
have a concept of the *current directory*
Directory is the older term for folder from when there were not pictures of
folders in a graphical interface.  

You start in your home directory.  My login id is anh, so my home directory is 
``/Users/anh``.  Substitute your login id for your machine.
The slashes separate nested directories.  The top hard drive
directory is ``/``, which contains the directory ``Users`` which contains
users' home directories, like my ``anh``.  A shorthand in a terminal for your home directory
is ``~``.

The terminal shows a system prompt when it is ready for user input.  The prompt
can be set to show many things.  The end of the prompt is often ``$``.
Before that is often some indication of your current directory, like ``~`` for
the home directory.

If you want to see the full name of the current directory enter the command

  pwd

Single commands are executed after you press the Enter key.

You can **l**\ i\ **s**\ t the contents of a directory with the ``ls`` command.
Unix tends to abbreviate words in commands.

If you use the ls command in your home directory, you should see 
``Desktop``, ``Documents``, ``Downloads``, ... listed.

To **c**\ hange **d**\ irectory, use the ``cd`` command followed by
the directory you would like to change to.  You can use the full
name of the directory starting with ``/``, but more commonly you just indicate
where to go relative to where you are now.  ``Desktop`` is a subdirectory of
your home directory, so from the home directory you can just enter

  cd Desktop
  
Here is a sequence on my computer after starting a terminal (skipping most 
of the output from ``ls``)

  | Last login: Sat May 19 18:03:19 on ttys001
  | anh@lucky13:~$ pwd
  | /Users/anh
  | anh@lucky13:~$ ls
  | 
  | ...
  | Desktop                          ...
  | Documents                        ...
  | Downloads                        ...
  | ...
  | 
  | anh@lucky13:~$ cd Desktop
  | anh@lucky13:~/Desktop$ pwd
  | /Users/anh/Desktop
  | anh@lucky13:~/Desktop$ cd ..
  | anh@lucky13:~$ pwd
  | /Users/anh
  | anh@lucky13:~$ 

Notice that the last use of the ``cd`` command used directory ``..``.
That stands for the parent directory, the directory containing the
current directory.

If you unzipped examples.zip from your Desktop, you can go to the exaples with

    cd ~/Desktop/examples
    
Alter this if you put your examples somewhere else!

It is useful to be in the examples folder.  If you start Idle from there,
it is easy to open any of the example programs.

When scripts are directly called by the operating system, they look
for the proper interpreter to read them.  Our scripts are set up to look for
python3. 

To start a regular python program from the current directory, like hello_you.py,
you would enter a command with python3 and the file name, like
 
   python3 hello_you.py
   
Instead of shifting to a separate Shell as in Idle, the output appears right in the 
terminal window.


