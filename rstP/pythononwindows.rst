.. index:: windows

 
Some Special Windows Instructions
==========================================

While the Python language changes slowly, operating systems and setup methods change 
more rapidly with succeeding versions.  
The attempt here is to keep all such information in one place for the Windows operating system.
It may become out of date at any time.

-- Last checked this on Windows 10 and Windows 7 with Python 3.7.

Versions
---------------

I will use Python 3.7+ to mean the current version of Python, with version number at least
3.7.4.  Make sure you have the latest recommended version installed from https://www.python.org/downloads/.  
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

You are encouraged to test if Python did get added to the environment by starting Idle
as discussed on the next section.

Starting Idle Shortcut
------------------------

If you want to start Idle without a starting file, 
but later deal with files in the examples folder,
then a one-step shortcut is to double click on the
file :file:`IdleOnWindows.cmd` in the examples folder.
If this does not work (in Windows),
then go back and modify your Python installation,
as discussed in the previous section.

If you want to do extensive Idle work in another folder, 
you can copy :file:`IdleOnWindows.cmd` to there and use it.

File Names in the File Explorer
--------------------------------

By default Windows does not display file extensions in File Explorer Windows.
You may have multiple files with the same base name but different
extensions.  Particularly if you want to attach one to an email or
homework submission, this can lead to problems.

You are strongly suggested to change the viewing default in File Explorer to show extensions.

Chapter 4 CGI Instructions 
-----------------------------

You can skip this until you are starting Chapter 4.4 on CGI files.

Opening .cgi Files in Idle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By convention the server programs that you will be writing end in ".cgi".
That is not an extension that is automatically associated with Idle for editing.
If you want to open a .cgi file (or any other type but .py)
to edit (and never run) from inside of Idle, it is possible to do this directly in many
steps, but it is easier to go indirectly:  

*  Start a .py file you have in Idle (like localCGIServer.py), 
   or if :file:`IdleOnWindows.cmd` is there, as in my www folder, 
   use it to start Idle.
*  To open a .cgi file
   from *inside* Idle, you select Open form the File menu like normally, but then
   notice the drop-down choice in the lower right of the file open window that
   probably shows Python files (*.py):  Change this file filter to All files (*.*).
*  Then all files in the current folder should be listed, not grayed out,
   and you can navigate to and choose the one you want. 

Saving a new .cgi file
~~~~~~~~~~~~~~~~~~~~~~~~

As with opening a .cgi file, set the format filter at the bottom of the dialog window to
All files (*.*).  Then enter the full file name with the .cgi.
If you forget and do not change the file filter, a ".py" will be added to your file name.
Then you can rename it in File Explorer.


Running CGI Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
If you insist on doing cgi work in a different folder, copy both startServer.cmd and localCGIServer.py 
as well as all related .html and .cgi files to that folder, 
and then when you want to test your work, start the local server from *there* with startServer.cmd.

At this point you can do all the web server based activities in Chapter 4.
There are a number of steps: be sure you carefully go through the list in the tutorial.
Remember, html files calling a cgi file, and cgi files used directly are *only* run in your web browser
with a URL starting with localhost:8080/, and only *after* you have a local server running
from the *same* folder.  Otherwise nothing dynamic happens.

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



