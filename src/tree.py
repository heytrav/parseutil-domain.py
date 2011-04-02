'''
Created on Mar 20, 2011

@author: holton
'''

class Tree(object):
    '''
    Some docs
    '''


    def __init__(self, rootNode = None, 
                 wildcard = "*", replaceWildcard = "[^\.]+", 
                 separator = ".", replaceSeparator = "\.",
                 endOfPath = "\b"):
        '''
        Some docs
        '''
        
        self.__node = rootNode
        self.children = {} # dict
        self.__parent = None
        self.__depth = 0
        self.wildcard = wildcard
        self.replaceWildcard = replaceWildcard
        self.separator = separator
        self.replaceSeparator = replaceSeparator
        self.endOfPath = endOfPath
        self.terminalNodes = []
                
        
    def add(self, childNode): # not used?
        childNode.parent(self)
               
    def addBranch(self, newPath): # subclassed
        return           
        
    
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
            return self.getNodeValue()
        elif len(self.children.keys()) > 0:
            childNodes = []
            for childNode in self.children.values():
                childDataStructure = childNode.getSubDataStructure()
                childNodes.append(childDataStructure)
            datastructure = {}
            datastructure[self.getNodeValue()] = childNodes
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
            return self.endOfPath
        elif node == self.wildcard:
            return self.replaceWildcard
        elif node == self.separator:
            return self.replaceSeparator
        return node
  