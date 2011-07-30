'''
Created on Mar 13, 2011

@author: holton
'''

import re 
import sys
import getopt

from treefix import rgxnode



options = getopt.getopt(sys.argv[1:], 'i:c')
suffixfilename = ''
compression = False
for option, value in options[0]:
    if option == '-i': suffixfilename = value
    if option == '-c' : 
        compression = True


compiledRegex = re.compile('''
  ^
    ( 
       [^\s\/\!][^\s]+
    )
  $
''', re.VERBOSE|re.MULTILINE
)


content = open(suffixfilename).read()
iter = re.finditer(compiledRegex, content)

node = rgxnode.RegexNode(applyCompression = compression)

for i in iter:
    node.addBranch(i.group(1))



regexed = node.regexify()

print regexed





    
        
