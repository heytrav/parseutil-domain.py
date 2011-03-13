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



print suffixfilename
content = open(suffixfilename).read()
print content
