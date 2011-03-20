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
        self.children = []
        self.__parent = None
        self.__depth = 0
        self.wildcard = wildcard
        self.replaceWildcard = replaceWildcard
        self.separator = separator
        self.replaceSeparator = replaceSeparator
        self.endOfPath = endOfPath
                
        
    def add(self, childNode):
        self.children.append(childNode)
        childNode.parent(self)
               
    def addBranch(self, newPath):
        # implementation to follow
        partitioned = newPath
        
    
    def parent(self, parentNode):
        self.__parent = parentNode
        
        
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
             
    def getSubTree(self):
        indent = ""
        for i in range(0, self.getDepth()):
            indent += " "
        prettyPrint = indent + self.__str__()
        for child in self.children:
            childString = "\n" + child.getSubTree()
            prettyPrint += childString
        return prettyPrint        
 
 
    def getNodeValue(self):
        return self.__node
 
    
    def isLeaf(self):
        if len(self.children) > 0:
            return False
        return True
      
                      
        
    def __str__(self):
        node = self.__node
        if node == self.wildcard:
            return self.replaceWildcard
        elif node == self.separator:
            return self.replaceSeparator
        return node
  