'''
Created on Mar 20, 2011

@author: holton
'''

class Tree(object):
    '''
    Some docs
    '''


    def __init__(self, 
                  rootNode       = None,
                 wildcard =   None, 
                 replaceWildcard = None, 
                 separator = None, 
                 replaceSeparator = None,
                 endOfPath = None, 
                ):
        '''
        Some docs
        '''
        
        self.__node = rootNode
        self.children = {} # dict
        self.__parent = None
        self.__depth = 0
        self.__wildcard = wildcard
        self.__replaceWildcard = replaceWildcard
        
        self.__separator = separator
        self.__replaceSeparator = replaceSeparator
        self.__endOfPath = endOfPath
        self.terminalNodes = []
                
        
    def add(self, childNode): # not used?
        childNode.parent(self)
               
    def addBranch(self, newPath): # subclassed
        return           
        
    def getWildcard(self):
        return self.__wildcard
    
    def getReplaceWildcard(self):
        return self.__replaceWildcard
    
    def getSeparator(self):
        return self.__separator
    
    def getReplaceSeparator(self):
        return self.__replaceSeparator
    
    def getEndOfPath(self):
        return self.__endOfPath
    
    def parent(self, parentNode):
        self.__parent = parentNode
        
    def setNodeValue(self, nodeValue):
        myNode = self.__node
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
            path.append(self.endOfPath)
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
            
        for child, offspring in self.children.items():
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
            
        
        
            
            
 
    def consolidate(self):
        return
        
 
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
            return self.getEndOfPath()
        elif node == self.getWildcard():
            return self.getReplaceWildcard()
        elif node == self.getSeparator():
            return self.getReplaceSeparator()
        return node
  