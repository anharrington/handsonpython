 
Some Special Current Windows Instructions
==========================================

I have checked this on Windows 10 and Windows 7.

*This document supersedes any conflicting instructions in the tutorial itself.*
As versions of Python and operating systems have changed, some old usage instructions get out
date, and it is easier to maintain all such changes in one focused document.  

Versions
---------------

I will use Python 3.7+ to mean the current version of Python, with version number at least
3.7.3.  Make sure you have the latest recommended version installed from https://www.python.org/downloads/.  
Download the Windows version.   
*Read this section before doing any installation.*  In particular note paragraph below with italics in it.

If the only option is to save it, agree, and find it in your download folder and double click to execute it.  If you have an option to immediately run on download, you can choose that. 

You are likely to get a security message before running.  Click Run.  

Pay attention:  *before clicking on Install Now*, note if there are check-boxes at the bottom of a window you see.  Make sure *both* are checked, about the Python Launcher AND to add Python to environment variables.
 
The final screen that you reach in the installation
links to more advanced references than we will want in this course, so probably skip them for now.

Python now behaves differently if you installed a previous version before (like me).  I could have missed something for someone installing Python for the first time.  Feel free for me to watch you while you share your screen in Zoom.

If you install Python *without* putting a check mark on Add Python to environment variables, then you can go back and fix it.  This is important for Ch 4:

#. Run the Python installation script again.  Since python is already there it looks different when it starts - 
   the first option is modify; click on that.
#. Just click Next on the second screen
#. On the following screen is where you make a change:  Click to put a checkmark in front of the line saying:
     
     Add Python to environment variables.

   Then click next/continue/finish - whatever to just advance to the end.

Now for section 4.4, when you double click on startServer.cmd in the www folder, you should see a window come up and stay, saying that the local server is started.  



Your Login ID
--------------

The normal place for you to have my examples folder is under your home folder, 
which has the same name as your Login ID. If you are just creating a login ID, 
it will save some hassle in Chapter 4, if your login ID does 
*not have a space in it*.
"Andy" or "anh" or AndyHarrington" would be fine for me, but  

   "Andy Harrington" 
   
would bomb the server in Chapter 4.

.. _blank-in-id:

If You Have a Blank in your Login ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The local server program central to chapter 4 bombs with
folder paths with a blank in the name.  

If you have a blank in your Login ID, it is not so easy to change.
Instead make a folder outside of your home folder:

#.  In the File Explorer go to This PC or Computer and select C: drive.
#.  Create a new folder and give it a name without blanks, like comp150.
    I suggest that you move my examples folder, or just the sub-folder 
    www so it is under your new folder.  For Chapter 4
    test my examples and add your work there.


.. _examples-folder:

Folder For My Examples
-----------------------

Wherever you plan to unzip my Python examples folder from
http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
you need to make sure that
my www folder, and any other folder where you put later .cgi files
does not have a blank in its name, 
*or any folder in which it is a sub-folder*.
If you have a "comp 150" folder, you might rename it "comp150".


Running VS. Editing
---------------------

Python files can be either run or opened for editing.


.. _edit-by-default:

Editing by Default
~~~~~~~~~~~~~~~~~~~~

You will be working mostly with files ending in .py -- Python source files.  
Most of the time you will be editing them and running them in IDLE, so the best
default behavior when opening a file with extension .py is to have it open in
Idle 3.7+.  

To open a python file from the File Explorer window with Idle

*  You may be able to double click on the file in Explorer (or that may execute the program, 
   and then likely have its window immediately disappear)
*  If that is not set right, right click on the file, 
   select Edit with Idle, and click on the sub-menu for Idle that opens.
 
Idle can also be opened by going to All Programs with the Windows Start menu, 
opening Python 3.7+, and selecting Idle.  
This is OK if you just want to play with the Python shell window.  
If you want to open or particularly if you want to save a file 
there is the *major* disadvantage of the current folder 
being the Python system folder.  
*Saving a file with the wrong name there can totally screw up Python* 
(and has - and has been awful to debug).

For earlier versions of Python on Windows (3.4), the tutorial still refers to a shortcut
for opening Idle.  Such shortcuts do not work in 3.5 or 3.6.  
Ignore the file and any description of it, and use the methods above to open a Python file.
 

Inside IDLE
--------------
   
Opening/Creating Files from Inside Idle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may select Open in the File menu *inside* Idle, either with the Shell window
or a file editing window as the active window.  The folder that it expects the file 
to reside in depends on the window you started from:

*  If your current window is a file editing window, the folder that you see
   will when you go to open a file 
   is the same folder as the current file.
*  If your current window is the Python Shell window, and you opened it from the
   Start Menu as discussed above, then be very careful!  The associated folder is the Python 
   system folder, and you can get really mess things up trying to save a file there!
   Be sure to change to a folder you control.

Behavior is similar if you go to the File menu inside Idle to create a totally New
file:  when you go to save it later, the folder you will see will be selected just as when you
opened a file above.

Saving Files
~~~~~~~~~~~~

If you have modified a file and want to save it under a new name, make sure
the file is in the active window (you are not in the shell window), go to
the File menu and Save. It is easiest if
you save all files in the same folder: my examples folder (except in Chapter 4).

Running Program Files
~~~~~~~~~~~~~~~~~~~~~

Make the Edit window for the file you want active by clicking in its window, 
then go to the Run
menu and select Run Module. Note the F5 shortcut key.


Chapter 4 CGI Instructions 
-----------------------------

You can skip this until you are starting Chapter 4.4 on CGI.

Remember this is the time when it is critical not to have .cgi files under a folder
with a blank in the name.  See the earlier discussion.

CGI Files on My Server Do Not Work!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The administrators of my server changed the security parameters, so now the 
*links to run cgi scripts on my internet server do not work.*  
Just use the ones 
for the local server on *your* machine, as discussed below, 
starting with localhost:8080/.

Opening .cgi Files in Idle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By convention the server programs that you will be writing end in ".cgi".
That is not an extension that is automatically associated with Idle for editing.
If you want to open a .cgi file (or any other type but .py)
to edit (and never run) from inside of Idle, it is possible to do directly in many
steps, but it is easier to go indirectly:  

*  Start a .py file you have in Idle (like localCGIServer.py) (or go from the Windows Start menu)
*  To open a .cgi file
   from *inside* Idle, you select Open form the File menu like normally, but then
   notice the drop-down choice in the lower right of the file open window that
   probably shows Python files (*.py):  Change it to All files (*.*).
*  Then all files in the current folder should be listed, 
   and you can navigate to and choose the one you want. 


Running CGI Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you create and
edit a cgi file inside Idle, remember you *cannot run it* from inside
Idle.  Besides editing there is one thing you can and should
do after editing: be **sure** to check the syntax, 
using alt-X, or else you will get zero feedback on syntax errors.

When you want to test a cgi script, you first need to have launched
the local CGI Server.  Note that 
localCGIServer.py can be run from inside Idle, 
but then running any other program inside Idle kills the local server.  

You can also start the local server and keep it running as long as you want to 
run .cgi files in that same folder, by double clicking on ``startServer.cmd`` 
which I have placed in the example www folder.  
(Note there is a separate Mac/Linux file, ``cgiServerScript``: 
do not try to use that!)
 
If you insist on doing cgi work in a different folder, copy both startServer.cmd and localCGIServer.py 
as well as all related .html and .cgi files to that folder, 
and then when you want to test your work, start the local server from *there* with startServer.cmd.

At this point you can do all the web server based activities in Chapter 4.
There are a number of steps: be sure you carefully go through the list in the tutorial.
Remember, html files calling a cgi file, and cgi files used directly are *only* run in your web browser
with a URL starting with localhost:8080/, and only *after* you have a local server running
from the same folder.  Otherwise nothing dynamic happens.

.. wait and fix?

    Terminal Use (Optional)
    ----------------------------------

    To use the Hands-on Python Tutorial, the information above should be sufficient
    to get your usage going.  Terminals are quite useful in other contexts:
    There are many things that can be
    done from such a window that cannot be done from the File Explorer or with an App.

    If you would like a bit more background, read on.

    Navigation
    ~~~~~~~~~~~~

    Windows has a concept of the *current directory*
    Directory is the older term for folder from when there were not pictures of
    folders in a graphical interface.  

    You start in your home directory.  My login id is anh, so my home directory is 
    ``\Users\anh``.  Substitute your login id for yours.
    The slashes separate nested directories.  The top hard drive
    directory is ``\``, which contains the directory ``Users`` which contains
    users' home directories, like my ``anh``.  

    The terminal shows a system prompt when it is ready for user input.  The prompt
    can be set to show many things.  The end of the prompt is often ``>``.
    Before that is often some indication of your current directory.

    Single commands are executed after you press the Enter key.

    You can get a **dir**\ ectory of the contents of a directory with the ``dir`` command.

    If you use the ls command in your home directory, you should see 
    ``Desktop``, ``Documents``, ``Downloads``, ... listed.

    To **c**\ hange **d**\ irectory, use the ``cd`` command followed by
    the directory you would like to change to.  You can use the full
    name of the directory starting with ``\``, but more commonly you just indicate
    where to go relative to where you are now.  ``Desktop`` is a subdirectory of
    your home directory, so from the home directory you can just enter

      cd Desktop
      
    Here is a sequence on my computer after starting a terminal (skipping most 
    of the output from ``dir``::

        Microsoft Windows [Version 10.0.10586]
        (c) 2015 Microsoft Corporation. All rights reserved.

        C:\Users\cs>dir
         Volume in drive C has no label.
         Volume Serial Number is 0E71-00F5

         Directory of C:\Users\anh

        05/09/2016  12:29 PM    <DIR>          .
        05/09/2016  12:29 PM    <DIR>          ..
        05/09/2016  09:28 AM    <DIR>          Contacts
        05/09/2016  09:28 AM    <DIR>          Desktop
        05/09/2016  09:28 AM    <DIR>          Documents
        ...
        05/09/2016  09:28 AM    <DIR>          Saved Games
        05/09/2016  09:28 AM    <DIR>          Searches
        05/09/2016  09:28 AM    <DIR>          Videos
                       0 File(s)              0 bytes
                      15 Dir(s)  71,703,621,632 bytes free

        C:\Users\anh>cd Desktop

        C:\Users\anh\Desktop>dir
         Volume in drive C has no label.
         Volume Serial Number is 0E71-00F5

         Directory of C:\Users\anh\Desktop

        05/09/2016  09:28 AM    <DIR>          .
        05/09/2016  09:28 AM    <DIR>          ..
        05/09/2016  09:28 AM    <DIR>          examples
                       0 File(s)              0 bytes
                       3 Dir(s)  71,703,621,632 bytes free

        C:\Users\anh\Desktop>cd ..

        C:\Users\anh>

    Notice that the last use of the ``cd`` command used directory ``..``.
    That stands for the parent directory, the directory containing the
    current directory.

    If you unzipped the examples from your Desktop, you can go there with

        cd Desktop/examples
        
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



