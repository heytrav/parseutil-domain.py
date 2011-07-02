'''
Created on Mar 13, 2011

@author: holton
'''

import re 
import sys
import getopt

from treefix import node


def reverseLevel(tldSequence):
    segments = tldSequence.split(".")
    if len(segments) > 1:
        segments.reverse()
    
    return segments

def idnEncodeSegments(subTld):
 
    unicodeTld = unicode(subTld,"utf8")
    idnEncoded = u''
    
    try:
        idnEncoded = unicodeTld.encode("idna")
    except UnicodeError, e:
        #print "Error processing " + subTld
        #print e
        return None
    return idnEncoded


def regexify(data):
    if isinstance(data, dict):
        iter = data.iteritems()
        k, childNodes = iter.next()
        joinedString = "|".join([regexify(i) for i in childNodes])
        return k + "(?:" + joinedString + ")"
    else:
        return data
    

options = getopt.getopt(sys.argv[1:], 'i:c')
suffixfilename = ''
compression = False
for option, value in options[0]:
    if option == '-i': suffixfilename = value
    if option == '-c' : 
        compression = True
        print "Setting compression to: " , compression

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

node = node.Node(
                 wildcard = "*", 
                 replaceWildcard = "[^\.]+", 
                 separator = ".", 
                 replaceSeparator = "\.",
                 endOfPath = "\b",
                 applyCompression = compression
                 )

for i in iter:
    reversedTldArray = reverseLevel( i.group(1) )
    idnProcessed = []
    for j in reversedTldArray:
        encoded = idnEncodeSegments(j)
        if encoded is not None:
            idnProcessed.append(encoded)
    
    reversedTld = ".".join(idnProcessed)
    
    if len(reversedTld) > 0:
        node.addBranch(reversedTld)



consolidated = node.consolidate()

#print consolidated.getSubTree()

regexified = regexify(consolidated.getSubDataStructure())
print regexified
tldregex = re.compile(regexified)






    
        
