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
                
        
    def add(self, childNode): # not used?
        childNode.parent(self)
               
    def addBranch(self, newPath): # subclassed
        return
            
            
        
    
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
        
        for child,offspring in self.children.items():
            subtree = offspring.getSubTree()
            childString = "\n" + subtree
            prettyPrint += childString
        return prettyPrint        
 
 
    def getNodeValue(self):
        if self.__node is None:
            return self.endOfPath
        return self.__node
 
    
    def isLeaf(self):
        if len(self.children) > 0:
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
  