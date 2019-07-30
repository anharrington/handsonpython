#!/usr/bin/env python3

'''
Remove line putting final genindex word in pdf
'''

import sys

badline = r'\emph{genindex}'
def removegenindex():

    fname = sys.argv[1]
    with open(fname) as f:
        s = f.read()
    s = s.replace(badline, '')
    with open(fname, 'w') as f:
        f.write(s)
        
removegenindex()
