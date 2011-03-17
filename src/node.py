'''
Created on Mar 16, 2011

@author: holton
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, nodeValue):
        '''
        Constructor
        '''
        self.__node = nodeValue
        self.children = []
        self.__parent = None
        self.__depth = 0
        
    
    def add(self, childNode):
        self.children.append(childNode)
        childNode.parent(self)
    
    def parent(self, parentNode):
        self.__parent = parentNode
        
     
    def isLeaf(self):
        if len(self.children) > 0:
            return False
        return True
    
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
            path.append("$")
        return path
             
           
        
    def __str__(self):
        indent = ""
        for i in range(0, self.getDepth()):
            indent += " "
        prettyPrint = indent + self.__node
        for child in self.children:
            childString = "\n" + child.__str__()
            prettyPrint += childString
        return prettyPrint
        
        
    # Comparison methods    
    def __eq__(self, other):
        return self.__node == other.__node
    
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
    
    
