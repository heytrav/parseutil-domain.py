'''
Created on Mar 16, 2011

@author: holton
'''



class Node(object):
    '''
    Represent tree like structures.
    '''
    parentSets = {}
    subtreeSets = {}
    nodeNumber = 0

    def __init__(self, 
                 nodeValue = None,
                 wildcard = None, 
                 replaceWildcard = None, 
                 separator = None,
                 replaceSeparator = None,
                 applyCompression = None,
                 escapeChars = None,
                 endOfPath = ""
                 ):
        '''
        Node()
        Node(
                 wildcard         = "*", 
                 replaceWildcard  = "[^\.]+", 
                 separator        = ".", 
                 replaceSeparator = "\.",
                 endOfPath        = "\b"
        )
        '''
         
        self.__node = nodeValue
        self.children = {} # dict
        self.__parent = None
        self.__depth = 0
        self.__wildcard = wildcard
        self.__replaceWildcard = replaceWildcard

        self.__separator = separator
        self.__replaceSeparator = replaceSeparator
        self.__endOfPath = endOfPath
        self.__commonSubtrees = dict()
        self.__applyCompression = applyCompression
        self.__escapeChars = escapeChars
        self.terminalNodes = []

     
     
    def addBranch(self, newBranch):
        
        child, offspring = newBranch[0], newBranch[1:]
        if not self.children.has_key(child):
            childNode = Node(child,
                              self.__wildcard, 
                              self.__replaceWildcard,
                              self.__separator,
                              self.__replaceSeparator,
                              self.__applyCompression,
                              self.__endOfPath,
                             
                             )
            childNode.parent(self)
            self.children[child] = childNode
        else:
            childNode = self.children[child]
        if len(offspring) > 0:
            childNode.addBranch(offspring)
        
        
        
    def consolidate(self, hasSiblings = False):
        
        if self.isLeaf():
            # if we're the end of a leaf, return the value
            return self
        
        elif len(self.children.keys()) == 1:
            # if there is only one child, prepend ourself to their "value"
            # child may be a leaf, or it could be part of a "stem"
            # First pop it out of our hash

            child = self.children.keys()[0]
            childNode = self.children.pop(child)
            consolidatedChild = childNode.consolidate()

            if consolidatedChild is not None:
                consolidatedValue = consolidatedChild.__str__()
                newChildNodeString = self.__str__() + consolidatedValue
                if hasSiblings and self.__parent is not None:
                    # store this so we can consolidate parents later
                    self.__parent.appendCommonSubtree(
                                                      consolidatedChild, 
                                                      self.__str__()
                                                      )
                childNode.setNodeValue(newChildNodeString)
                childNode.children = consolidatedChild.children
              
                return childNode
  
        else:
            newChildren = {}
            replaceWithNodes = list()
            for childNode in self.children.itervalues():
                replaceWithNode = childNode.consolidate(True)
                replacementValue = replaceWithNode.__str__()
                newChildren[replacementValue] = replaceWithNode
                replaceWithNodes.append(replaceWithNode)
                
            if self.__applyCompression == True and len(self.__commonSubtrees) < len(self.children):
                # some of the direct children have identical offspring
                
                for commonKey in self.getCommonSubtrees().itervalues():
                    if len(commonKey) > 1:
                        commonKeySet = []
                        for nodeDict in commonKey:
                            # for each of the common keys, pop combined node 
                            # back out
                            charValue = nodeDict['currentNode']
                            commonKeySet.append(charValue)
                            commonChild = nodeDict['subNodeRoot']
                            newChildren.pop(charValue + commonChild)
                        multiKeyNode = Node(commonKeySet)
                        commonChildNode = Node(commonChild)
                        multiKeyNode.add(commonChildNode)
                        commonChildValue = commonChildNode.__str__()
                        multiKeyNode.children[commonChildValue] = commonChildNode
                        #commonKeyString = self.compactSetString(commonKeySet)
                        commonKeyString = "".join(commonKeySet)
                        print "got common keys: " , commonKeyString
                        newChildren[commonKeyString] = multiKeyNode
                        self.add(multiKeyNode)
                    
            else:
                for cnode in replaceWithNodes:
                    self.add(cnode)
            
            self.children = newChildren
            return self
        
    def compactSetString(self,characterSet):
        sortedChars = sorted(characterSet)
        print "Got keys: ", ", ".join(sortedChars)
        if len(sortedChars) == 2:
            return "".join(sortedChars)
        plusOneIndexes = []
        compactList = []
        nextChar = None
        for index in range(0, len(sortedChars) ):
            print "index: " , index
            currChar = sortedChars[ index ]
            print "curr char " + currChar
            if ( index + 1) < len(sortedChars):
                nextChar = sortedChars[ index + 1 ]
                print "next char " + nextChar
            else:
                nextChar = None
        
            print "length of index array: " , len(plusOneIndexes)     
            if  nextChar != None and ord(nextChar) - ord(currChar) == 1:
                print "difference is 1 between " + currChar + " and " + nextChar
                plusOneIndexes.append(index)
            
            elif len(plusOneIndexes) > 1:
                difference = len(plusOneIndexes)
                firstIndex = plusOneIndexes[0] 
                print "first index: ", firstIndex
                lastIndex = plusOneIndexes[-1] + 1
                print "last index: ", lastIndex
                firstChar = sortedChars[firstIndex]
                lastChar = sortedChars[lastIndex]
                joinedCharSet = "-".join([firstChar, lastChar])
                
                compactList.append(joinedCharSet)
                plusOneIndexes = []
                
            else:
                plusOneIndexes = []
                
        
        return "".join(compactList)
                
         
       
        
                
    def appendCommonSubtree(self, subtree, currentNode):
        subtreeRoot = subtree.__str__()
        subtreeString = subtree.getSubTree()
        if not self.__commonSubtrees.has_key(subtreeString):
            self.__commonSubtrees[subtreeString] = []
            
        self.__commonSubtrees[subtreeString].append(
                                                    {
                                                     'subNodeRoot':subtreeRoot,
                                                     'currentNode':currentNode
                                                     }
                                                    )  
        
        
    def getCommonSubtrees(self):
        return self.__commonSubtrees
    
        
    def getCommonSubtree(self, subtreeString):
        return self.__commonSubtrees[subtreeString]
     
         
    def add(self, childNode): # not used?
        childNode.parent(self)
    
    def parent(self, parentNode):
        self.__parent = parentNode
        
    def setNodeValue(self, nodeValue):
        self.__node = nodeValue 
        
    def getDepth(self):
        if self.__parent is None:
            return self.__depth
        depth = self.__parent.getDepth() + 1
        return depth
    
    def getPathFromRoot(self):
        if self.__parent is None:
            path = [self.__node]           
        else:
            path =  self.__parent.getPathFromRoot()
            path.append(self.__node)           
            
        if self.isLeaf():
            path.append(self.__endOfPath)
        return path
             
             
    def getSubTree(self, indentFactor = 1, 
                   indent = "", 
                   space = " ", 
                   multiSeparator = "\n",
                   frontFrame = "",
                   backFrame = "",
                   orSeparator = ""):
        for i in range(0, self.getDepth() * indentFactor):
            indent += space
        prettyPrint = indent + self.__str__()
        separator = ""
        if len(self.children.keys()) > 1:
            separator = multiSeparator
            indentFactor = 1
        else:
            indentFactor = 0
            
        for offspring in self.children.values():    #items():
            subtree = offspring.getSubTree(indentFactor)
            childString = separator +  subtree 
            prettyPrint +=  childString
        return  prettyPrint         
 
    def getSubDataStructure(self):
        
        if self.isLeaf():
            return self.__str__()
        elif len(self.children.keys()) > 0:
            childNodes = []
            for childNode in self.children.values():
                childDataStructure = childNode.getSubDataStructure()
                childNodes.append(childDataStructure)
            datastructure = {}
            datastructure[self.__str__()] = childNodes
            return datastructure
                       
            
 
 
    def getNodeValue(self):
        if self.__node is None:
            return self.endOfPath
        return self.__node
 
    
    def isLeaf(self):
        if len(self.children.keys()) > 0:
            return False
        return True
                 
        
    def __str__(self):
        node = self.__node
        if node is None:
            return self.__endOfPath
        elif isinstance(node, list):
            if self.__applyCompression == True:
                combined = self.compactSetString(node)
            else:
                combined = "".join(node)
            return "[%s]" % combined
        elif node == self.__wildcard:
            return self.__replaceWildcard
        elif node == self.__separator:
            return self.__replaceSeparator
        return node
         
        
               
    # Comparison methods    
    def __eq__(self, other):
        if self.isLeaf():
            if not other.isLeaf():
                return False
            return self.__node == other.__node
        elif other.isLeaf():
            return False
        return self.children == other.children
        
    
    def __ne__(self, other):
        return self.__node != other.__node
    
    def __lt__(self,other):
        return self.__node < other.__node
    
    def __gt__(self, other):
        return self.__node > other.__node
    
    def __le__(self,other):
        return self.__node <= other.__node
    
    def __ge__(self, other):
        return self.__node >= other.__node
    
    
