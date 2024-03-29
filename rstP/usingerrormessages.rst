.. index:: error types
   syntax error

Using Error Messages
====================

You can expect to make some errors while coding.  Idle provides
information about the location and type of errors in several ways,
depending on the kind of error.  To be most useful, you want to be
able to decode the error feedback.

To illustrate I start from a file that is purposefully incorrect to
show off debugging ideas::

    x = input("Enter a number")
    y = x + 10
    print('10 more is {}'.format(y)
    print('Now we are done!')

I also have an initial documentation line.  If I try to run this I get

.. figure:: images/invalidSyntaxPrint.*
   :align: center
   :alt: image
   :width: 350 pt

A pop-up Invalid Syntax window indicates the **syntax error** was found by the
interpreter in just trying to read the program - never getting to
execution.  It highlights ``print`` in pink, indicating this is where it
realized there was an error.  (I left a number of blank lines in my
program, so this image would show both the pop-up window and the
highlighted code.)

You should know that print statements are perfectly legal.  There does
not seem to be an issue with the word print.  Note carefully what I
said earlier:  This is where the interpreter *first noticed* there was
and error:  The actual error could be earlier - it just was not clear
there was one yet.  The most common earlier place is the previous
line, and I illustrated the most common such error.  The interpreter
did not find an error on the previous line because it did not realize
it was at the end of a statement.  When can a statement go on to the
next line?  - When there are unmatched grouping characters, most
commonly ( ).

It is very easy to have unmatched parentheses, particularly when there
are many levels of pairs of parentheses.  Recall that when you type in
Idle it shows you what closing parentheses match with.  Here is the
image just after I added the correct final ) at the end of the
previous line:

.. figure:: images/idleShowsMatchingParentheses.*
   :align: center
   :alt: image
   :width: 227.25 pt


I did not show the progress in entering this program with its error, but 
Idle would have given a clue.  If we back up to when the first
incorrect print line was entered, right after the enter key is pressed,
you would see

.. figure:: images/strangeCursorLocIndicatesError.*
   :align: center
   :alt: image
   :width: 227.25 pt

Note where the vertical bar cursor \| jumped to:  not the beginning of
the next line, where you would put the next statement.  If you look
where it is positioned relative to the previous line, it is just after
the unmatched opening parenthesis!  This is Idle's convention, so if you are
paying attention to the automatic cursor indent, you should realize
there was an error with unmatched delimiters, and see the issue.

Note that Idle also should give you warning of the opposite error: If
you add an excess close-parenthesis, you should hear a beep,
indicating it was not expecting that character.

So now assume we have done this correction to the program, adding the
closing parenthesis.  If we try to run again:

.. figure:: images/EOL_inStringLiteral.*
   :align: center
   :alt: image
   :width: 350 pt

Another syntax error, this time at the end of the last line, and with
more information about the error.  EOL stands for "End Of Line",  so
it got all the way to the end of the line reading a string literal. 
The coloring also indicates this:  green all the way to the end of the
line.  What does a string literal need at the end?  - A final matching
quote character!  And we need a closing parenthesis, remembering our
previous error.  Suppose I complete the line as  ::

    print('Now we are done!)')


.. index:: run time error

I can now try to run again.  This time we do not get a pop-up syntax
error window.  This means the interpreter did not find any errors
*reading* the program. 
Many errors are only found when running the program, so execution
starts in the shell, leading to a **run-time error**.  
The program first prompts for a number, and I
enter 100:

.. figure:: images/implicitConversionErrorTrace.*
   :align: center
   :alt: image
   :width: 480 pt

We have a red **error traceback**.  In this case the "back" is not clear: 
If there were many nested function calls (as in the final part of
this section) we would see all the lines that called the next uncompleted
function, plus the last line where the error was actually detected. 
It shows the line ::

    y = x + 10

In this little short program, it is easy to go back to the Python
source and locate the line.  Idle also gives you help with this in
general:  The next screen shows me right-clicking the mouse (or
control-click on a Mac) on top of the red "line 14", where it is
saying the error is.  This generates a pop-up window.

.. figure:: images/gotoErrorLine1.*
   :align: center
   :alt: image
   :width: 460 pt

The only allowed option is to select **Go to file/line**

.. figure:: images/gotoErrorLine2.*
   :align: center
   :alt: image
   :width: 260 pt

and then the focus jumps to the window with the source code, and
highlights the desired line:

.. figure:: images/gotoErrorLine3.*
   :align: center
   :alt: image
   :width: 227.25 pt

So we have the line with the execution error.  We still need to figure
out what is going on.  The bottom line of the red traceback
gave a description of
the error: 

    TypeError:   Can't convert 'int' object to str implicitly.

Think.  It is a type error, so look at the types.  It refers to an
int.  Clearly we have 10.  There is something about a string.  The
other data is ``x``.  What is its type?  Of course the prompt in the
previous line asks for a number, but what type is returned by the
input function?  -- always a string!  Look at the expression again
``x + 10`` -- a string plus a number  -- two different types, and it
cannot convert so they are the same implicitly.  So we need to be
explicit:  We want numeric addition, so we need two numbers, and the
string must be explicitly converted.  You might need to look that up,
but you have an idea what you are looking for:  we can use ``int`` as a
function to convert the string.  We do not need to add an extra line
-- we can make ``x`` start off as an ``int``, changing the first line to ::

    x = int(input("Enter a number"))

.. index:: logical error

We can go a bit further:  though running the original first line by
itself did not cause an error, looking at the output above, you can
see it is ugly, with the prompt running into the user response.  This
is a **logical error**.  It is easy to correct, changing the ending of the
first line prompt so we have ::

    x = int(input("Enter a number: "))
    y = x + 10
    print('10 more is {}'.format(y))
    print('Now we are done!)')

Now run again:

.. figure:: images/firstLineOutput.*
   :align: center
   :alt: image
   :width: 150 pt

One final logical error is the close-parenthesis in the output.  When
debugging, I added a required final quote character on the last line,
but I left an extra close-parenthesis.  In "fixing" the last line
earlier, I added another error.  I am illustrating that this is
unfortunately easy to do!  Final code::

    x = int(input("Enter a number: "))
    y = x + 10
    print('10 more is {}'.format(y))
    print('Now we are done!')

Final run:

.. figure:: images/lastLineOutput.*
   :align: center
   :alt: image
   :width: 150 pt

So we have illustrated all three kinds of errors:

-  Syntax errors detected with a pop-up window in Idle before the
   program executes
-  Run time errors causing a red traceback sequence in the Shell output
-  Logical errors that Python does not find, but we need to note and
   troubleshoot in the source code when the results are not what we want

I chose common simple errors, so hopefully you would have been able to
figure out the meaning of the error message.  That is a *lot* to expect
in general.  We are only gradually adding explanations of bits of
Python syntax.  You can easily make an error that Python interprets as
being based on a more advanced feature, so the error message makes no
sense to you. 

Even if you do understand the error message, you should get the
information about where the error occurred.  Hopefully a concentrated
look there will lead to you seeing the error and being able to correct
it. 

If you did not understand the original error message, then there is a
further useful step after you do figure it out (with or without
outside help): **Go back and consider the error message again.**  After
seeing what was actually wrong, the error message may make sense now,
AND that knowledge may be useful to speed up your understanding and
your fix the next time you see that error message.

Particularly as a beginner, you can still hit a brick wall some of the
time, even with a partner.  You are also in a course with an
instructor:  that is a major reason I am here. Ask for help if
considering the information provided by Idle, plus a little thought, are
not enough!

.. index:: traceback


Nested Calls in Traceback
~~~~~~~~~~~~~~~~~~~~~~~~~

One more silly example program with an error, showtraceback.py,
to illustrate nested
function calls shown in an error traceback:

.. literalinclude:: ../examples/showtraceback.py 

.. no need

   .. figure:: images/showTracebackError.*
      :align: center
      :alt: image
      :width: 450 pt

Note that the first call to invminus4, with parameter 6, is fine: 
1.0/(6-4) = 0.5.
In the execution of the call ``invminus4(4)``, 
we get an error traceback message.  The image
below comes after the traceback is displayed, and then just as the
user uses the mouse to select the line where the error was:

.. figure:: images/tracebackAtError.*
   :align: center
   :alt: image
   :width: 450 pt

Note that after the title line in the traceback there are three
indented lines starting with "File", not just one line as in the
earlier program.  The bottom File line shows the line where the error
occurred, and we could jump to the source, continuing from the step in
the previous image:

.. figure:: images/source_error_highlighted.*
   :align: center
   :alt: image
   :width: 450 pt

The error takes place in a function, and a function can be called in
many places with different parameters. The further up lines in the
traceback show the **chain of function calls** to reach that occurrence of
the error.   The program calls main in the bottom line of the program
(line 13, first File line reference), and then main calls invminus4
twice.  We can tell which call caused the error, since the traceback
shows the call to ``invminus4`` at line 10.  If you had any question of
the context for any of the nested calls leading to the error, you
could also select a previous File line with the mouse, and jump to the
calling line in the source.

