'''
Created on Mar 13, 2011

@author: holton
'''

import re 
import sys
import getopt


options = getopt.getopt(sys.argv[1:], 'i:')
suffixfilename = ''
for option, value in options[0]:
    if option == '-i': suffixfilename = value

compiledRegex = re.compile('''
  
  \A
    ( 
       [^\s\/].*
    )

  \z

''', re.VERBOSE)

print suffixfilename
content = open(suffixfilename).read()
