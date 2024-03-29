.. index:: context

.. _Context:
        
Context
====================

You have probably used computers to do all sorts of useful and
interesting things. In each application, the computer responds in
different ways to your input, from the keyboard, mouse or a file.
Still the underlying operations are determined by the design of the
program you are given. In this set of tutorials you will learn to
write your own computer programs, so you can give the computer
instructions to react in the way *you* want.

.. index::
   machine language 
   high level language
   language - high level and machine
    
Low-Level and High-Level Computer Operations
--------------------------------------------

First let us place Python programming in the context of the
computer hardware. At the most fundamental level in the computer
there are instructions built into the hardware. These are very
simple instructions, peculiar to the hardware of your particular
type of computer. The instructions are designed to be simple for
the hardware to execute, not for humans to follow. The earliest
programming was done with such instructions. If was difficult and
error-prone. A major advance was the development of higher-level
languages and translators for them. Higher-level languages allow
computer programmers to write instructions in a format that is
easier for humans to understand. For example

    z = x+y

is an instruction in many high-level languages that means something
like:

#. Access the value stored at a location labeled x

#. Calculate the sum of this value and the value stored at a
   location labeled y

#. Store the result in a location labeled z.

No computer understands the high-level instruction directly; it is
not in *machine language*. A special program must first translate
instructions like this one into machine language. This one
high-level instruction might be translated into a sequence of three
machine language instructions corresponding to the three step
description above::

    0000010010000001  
    0000000010000010  
    0000010110000011 

Obviously high-level languages were a great advance in clarity!

If you follow a broad introduction to computing, you will learn
more about the layers that connect low-level digital computer
circuits to high-level languages.

.. index::
   Python; why 

.. _WhyPython:
    
Why Python
--------------------------

There are many high-level languages. The language you will be
learning is Python. Python is one of the easiest languages to learn
and use, while at the same time being very powerful: It is one of the most used languages by
highly productive professional programmers. 
Also Python is a
free language! If you have your own computer, you can download it
from the Internet....

.. index:: Python; downloading and installing
   
.. _getPython:

Obtaining Python for Your Computer
----------------------------------

Even if you have Python on your own computer, you may well not have the latest version.

If you think you already have a current Python set to go, then try starting Idle:
:ref:`Starting-Idle`.  If Idle starts, see if the version stated near the 
top of its window matches the latest
version of Python, then fine!

Otherwise, if you are using Windows or a Mac, see the :doc:`appendices` for instructions for 
individual operating systems.

Linux
   An older version of Python is generally installed, and even if
   a current version, 3.1+, is installed, Idle is not always
   installed. Look for a package to install,
   something like 'idle-python' (the name in the
   Ubuntu distribution).


Philosophy and Implementation of the Hands-On Python Tutorials
--------------------------------------------------------------

Although Python is a high-level language, it is *not* English or
some other natural human language. The Python translator does not
understand "add the numbers two and three". Python is a formal
language with its own specific rules and formats, which these
tutorials will introduce gradually, at a pace intended for a
beginner. These tutorials are also appropriate for beginners
because they gradually introduce fundamental logical programming
skills. Learning these skills will allow you to much more easily
program in other languages besides Python. Some of the skills you
will learn are

-  breaking down problems into manageable parts

-  building up creative solutions

-  making sure the solutions are clear for humans

-  making sure the solutions also work correctly on the computer.

.. index:: guiding tutorial principals
   single: *; important tutorial problem
   single: **; challenging tutorial problem

Guiding Principals for the Hands-on Python Tutorials:

-  The best way to learn is by active participation. Information is
   principally introduced in small quantities, where your active
   participation, experiencing Python, is assumed. In many place you
   will only be able to see what Python does by doing it yourself (in
   a hands-on fashion). The tutorial will often not show. Among the
   most common and important words in the tutorial are "Try this:"

-  Other requests are for more creative responses. Sometimes there
   are Hints, which end up as hyperlinks in the web page version, and
   footnote references in the pdf version. Both formats should
   encourage you to think actively about your response first before
   looking up the hint.
   The tutorials also provide labeled exercises, for further practice,
   without immediate answers provided. The exercises are labeled at
   three levels

   No label
     Immediate reinforcement of basic ideas - 
     *preferably do on your first pass*.

   \*
     Important and more substantial - be sure you can end
     up doing these.  Allow time to do them!

   \*\*
     Most creative

-  Information is introduced in an order that gives you what you
   need as soon as possible. The information is presented in context.
   Complexity and intricacy that is not immediately needed is delayed
   until later, when you are more experienced.

-  In many places there are complications that *are* important in
   the beginning, because there is a *common* error caused by a slight
   misuse of the current topic. If such a common error is likely to
   make no sense and slow you down, more information is given to allow
   you to head off or easily react to such an error.

Although this approach is an effective way to introduce material,
it is not so good for reference. Referencing is addressed in
several ways:

-  Detailed Table of Contents

-  Extensive Index in the web page version

-  Flexible Search Engine built into the html version
   (does *not* work on an html version that you download to your computer)

-  Cross references to sections that elaborate on an introductory
   section.  Hyperlinks allow you to jump between the referenced parts
   in the html version or the pdf version viewed on a computer.
   The pdf version also gives page references.

-  Concise chapter summaries, grouping logically related items,
   even if that does not match the order of introduction.


Using the Tutorial - Text and Video
-----------------------------------

The Hands-on Python Tutorial was originally a document to read,
with both the html version and a pdf version.
Even if you do not print it, some people use the pdf version online,
preferring its formatting to the formatting in the html version.

Some people learn better visually and verbally from the very
beginning.  The Tutorial has  800 by 600 pixel videos for many sections.

Also mentioned for the convenience of my Comp 150 class are videos beyondPython, 
for the part of the class after Python.

The videos are in two places:

*   `OneDrive <https://loyolauniversitychicago-my.sharepoint.com/:f:/g/personal/aharrin_luc_edu/EsF_0EGwnmFApwhmnHjNVAkBKxrfZcyQN1pFt-AK2yqMbQ?e=K2l8S9>`_.
    There are five zip files of videos that you can download and unzip:  one zip file for each chapter of the Python Tutorial (other than apendicies) and one for the remainder of the class (BeyondPython).
  

    Download split in 5 parts, with no ID needed at all.
    The four chapters of the Hands-on Python Tutorial (other than appencices) 
    and beyondPython 
    are collected in zip files for you to download, and then *expand* 
    the zip files before using.   

*   Google Drive: 
    https://drive.google.com/drive/folders/0B5WvvnDHeaIYMGE2MzU4OWEtYzQ4Zi00YzhiLTliMTItNjRjYzMyYzgyMTk2?usp=sharing
    
    You need a Google Drive/Docs login ID. 
    If you are not already logged into Google Drive/Docs, you will need to do it when
    you click on the link.
    If you have that ID, 
    then the advantage of Google Drive is that you can select exactly what parts to 
    view or download.  
    This may not work with Internet Explorer, 
    but it does work with Firefox, Safari or Chrome browser.  
	
To get the most out of the tutorial, I strongly suggest the following
approach for each part:

-  Watch a video if you like.  They are clearly labeled by numerical section.
   Stop the video where I ask you to *think*.
   The videos hit the high points and take advantage of being able to point
   at specific places on the screen.  They are not as recent as the current text,
   so they may look a bit different than the tutorial  in a web page.
   
   Some details may only appear
   in the written text.

   Stop the video
   frequently to test things for yourself!  If a new function is introduced,
   do not only watch the video, but try it out for yourself, including with data not
   in the video.  In some places the written version mentions more
   examples to try.  I suggest looking at the written version after each video.

-  Whether you look at the video of a section or not, do look through
   a written version, either as a first pass or to review and fill
   in holes from the videos.  Be sure to stop and try things yourself,
   and see how they actually work on your computer.

-  Look at the labeled exercises.  You are strongly recommended to
   give the unstarred ones an immediate try to reinforce basic concepts.
   The starred ones (*) are important for a strong understanding.  Do not get
   too far ahead in reading/watching before trying the starred exercises.
   Understanding earlier parts well enough to be able to solve problems
   is going to either be completely necessary for understanding some
   later sections or at least make later sections easier to follow
   and fully comprehend.

-  Python provides too rich an environment to be able to show you all
   interrelationships immediately.  That can mean errors send you in
   a strange (to you) direction.  See the appenidix section
   :doc:`usingerrormessages`.
   
Have fun and be creative, and discover your power with Python!

.. index:: problem solving

.. _learning-to-problem-solve:

Learning to Problem-Solve
--------------------------

While the tutorial introduces all the topics, there is more to say about
using it effectively.  There is way too much detail to just absorb all
at once,  So what are the first things to learn? 

More important than memorizing details is having an idea of the building
blocks available and how they are useful.  For the most direct
exercises, you might just look back over the most recent section
looking for related things, but that will not work when you have scores
of sections that might have useful parts!  The basic idea of the
building blocks should be in your head. For instance, 
looking ahead to when you have finished the
Tutorial through 1.10.4, you will want to have these ideas very present
in your head:

* You can use numbers and do arithmetic.
* You can store and retrieve data using variable names and assignment statements.
* Python has many useful built-in functions that can affect the system or return 
  results for you to use.
* You can get keyboard input from the user and print things back for the user.
* Data comes in different types, and you can convert where it makes sense.
* You can use strings and generate them in many ways:  
  literal strings, concatenation operator (+), string format method.

Once you have an idea of the appropriate building blocks needed to solve
a specific problem, then you can worry about more details.  Particularly
at the beginning, you are not likely to have all the exact Python syntax
for the parts of your solution nailed down!  It is not important to
remember it precisely, but it is important to know how to find a clear
explanation efficiently:  Know the location in examples or in the
tutorial, or use the index, the search capacity, summaries, and/or write
things in notes for yourself - as for an exam.  Writing short bits down
is also useful because the *act of writing* helps many people absorb what
they are writing.

As your experience increases you will get used to and remember more and
more stuff, but there is always the latest idea/syntax to get used to!
Your notes of what is important, but still not in immediate recall, will
evolve continuously.

This multi-tiered approach means that what you absorb should not just be
an enormous collection of unstructured facts that you plumb through in
its entirety to find a useful idea.  You first need to be particularly
aware of the major headings of useful features, and then do what you
need to drill down to details as necessary.

This approach is important in the real-world, away from Python.  The
world is awash with way to much information to memorize, but you must
access the information that you need to synthesize and formulate
solutions/arguments ... effectively!

Knowing all the building blocks of a solution is obviously important.  
Many successful holistic thinkers can do this effectively.  In some
domains a knowledge of the pieces and their relationships is enough.
Programming requires more than this, however:  It is critical to sort out 
the exact *sequence* in which the pieces must logically appear.  
Some excellent holistic thinkers have a hard time with this sequencing,
and must pay extra attention when planning code.  If you are like this, be patient
and be prepared to ask for help where needed.

What to do *after* you finish an exercise is important, too.  
The natural thing psychologically,
particularly if you had a struggle, is to think, "Whew, outta here!!!!"

On something that came automatically or flowed smoothly, that is not a big deal - 
you will probably get it just as fast the next time. 
If you had a hard time and only eventually
got to success, you may be doing yourself a disservice with "Whew, outta here!!!"

We have already mentioned how not everything is equally important, 
and some things are more important to keep in your head than others.  
The same idea applies to all the steps in solving a possibly long problem.  
Some parts were easy; some were hard; there may have been several steps.
If all of that goes into your brain in one continuous stream of stuff that you 
remember at the same level, then you are going to leave important nuggets mixed in
with an awful lot of unimportant and basically useless information.  Then the
information is likely to all fade into oblivion, or be next to 
impossible to cycle through looking for the useful nuggets.  
Why do the problem anyway if you are just going to bury important information further
down in your brain?

What is important?  
The most obvious thing you will need at a higher level of recall is what
*just messed you up*, what you missed until doing this problem:  After finishing the
actual problem, *actively* follow up and ask yourself:

- What did I get in the end that I was missing initially? What was the connection I made?
- Does this example fit in to some larger idea/abstraction/generalization in a way that
  I did not see before?
- How am I going to look at this so I can make a similar connection
  in a similar (or maybe only partly similar) problem?
- Is there a kernel here that I can think of as a new tool in my bag of tricks?
  
Your answers to these questions are the most important things to take away from your
recent hard work.  
The extra consideration puts them more in
the "priority" part of your brain, so you can really learn from your effort.  
When you need the important ideas 
next, you do not need to play through all the details of 
the stuff you did to solve the earlier problem.

Keep coming back to this section and check up on your process:  It is really important.


