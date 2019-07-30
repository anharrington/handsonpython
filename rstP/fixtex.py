#!/usr/bin/env python3

def fixTex(name): 
    with open(name) as f:
        s = f.read()
    # fix non-ascii
    s =s.replace('↤', 'for a left arrow').replace(
        '≤', '$\\leq$').replace('≥', '$\\geq$').replace('≠', '$\\neq$')

    # fix title page
    #fix title
##    b = s.index(r'\title')
##    p = s.index(r'\date', b)
##    print('>>>>>>>>>>>>old title\n' + s[b:p])
##    s = (s[:b] +
##         r'\title{Hands-On Python Tutorial}' + '\n' +
##         s[p:])
##
##    #fix release, author
##
##    with open('conf.py') as py:  # Python 2.6, not 3
##        conf = py.read()
##
##    start = "release = '"
##    b = conf.index(start) + len(start)
##    p = conf.index("'", b)
##    ver = conf[b:p]
##    print('ver =', ver)
##    
##    b = s.index(r'\release')
##    p = s.index(r'\newcommand', b)
##    print('>>>>>>>>>>old release, author\n' + s[b:p])
##
##    s = (s[:b] +
##         r'\release{' + ver + r''' For Python 3.1}
##\author{Dr. Andrew N. Harrington\texttt{}~\\
##\texttt{Computer Science Department\\
##Loyola University Chicago}~\\
##{\footnotesize © Released under the Creative Commons 
##Attribution-Noncommercial-Share-Alike 3.0 
##United States License}
##{\footnotesize \url{http://creativecommons.org/licenses/by-nc-sa/3.0/us/}}}
##''' + s[p:])
##
    # --------------------
    
    # remove repeat of stuff in index page in html
    b = s.index('Python 3.1 Version')
    p = s.index(r'\chapter', b)
    print('>>>>>>>>old index page stuff\n' + s[b:p])

    s = s[:b] +  s[p:]

    # remove ch 5 index and search - WRONG if get index working
##    b = s.rfind(r'\chapter')
##    p = s.rfind(r'\end')
##    print('ending junked\n' + s[b:p])
##
##    s = s[:b] +  s[p:]
         
    with open(name, 'w') as f:
        f.write(s)
    print('Wrote tweaks to', name)

import sys\\
\hline
\end{tabulary}

if __name__ == '__main__':
    fixTex(sys.argv[1])
    
##sub = r'''
##\title{Hands-On Python Tutorial}
##\release{0.5 For Python 3.1}
##\author{Dr. Andrew N. Harrington\texttt{}~\\
##\texttt{Computer Science Department\\
##Loyola University Chicago}~\\
##{\footnotesize © Released under the Creative Commons 
##Attribution-Noncommercial-Share-Alike 3.0 
##United States License}
##{\footnotesize \url{http://creativecommons.org/licenses/by-nc-sa/3.0/us/}}}
##'''


TEXineq = '''
\begin{tabular}{|c|c|c|}
\hline
\textbf{Meaning} 
& 
\textbf{Math Symbol} 
& 
\textbf{Python Symbols}
\tabularnewline
\hline

Less than

 & 
\textless{}

 & 
\code{\textless{}}

\tabularnewline

Greater than

 & 
\textgreater{}

 & 
\code{\textgreater{}}

\tabularnewline

Less than or equal

 & 
$\leq$

 & 
\code{\textless{}=}

\tabularnewline

Greater than or equal

 & 
$\geq$

 & 
\code{\textgreater{}=}

\tabularnewline

Equals

 & 
=

 & 
\code{==}

\tabularnewline

Not equal

 & 
=$\neq$

 & 
\code{!=}

\tabularnewline
\hline
\end{tabular}


'''
