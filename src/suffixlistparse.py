'''
Created on Mar 13, 2011

@author: holton
'''

import re 
import sys
import getopt


def reverseLevel(tldSequence):
    segments = tldSequence.split(".")
    if len(segments) > 1:
        segments.reverse()
    
    return segments


    

options = getopt.getopt(sys.argv[1:], 'i:')
suffixfilename = ''
for option, value in options[0]:
    if option == '-i': suffixfilename = value

compiledRegex = re.compile('''
  
  ^
    ( 
       [^\s\/\!].*
    )
  $

''', re.VERBOSE|re.MULTILINE)


content = open(suffixfilename).read()
iter = re.finditer(compiledRegex, content)
for i in iter:
    reversedTld = reverseLevel(i.group(1))
    if reversedTld is not None:
        
