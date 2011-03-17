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
        self.node = nodeValue
        self.children = {}
        self.parent = None
        
       
        
    
    def add(self, childNode):
        self.children.append(childNode)
        childNode.parent(self)
    
    def parent(self, parentNode):
        self.parent = parentNode
        
    def olderSibling(self,siblingNode):
        # implementation to follow
        return
    
    def youngerSibling(self, siblingNode):
        # implementation to follow
        return
        
    
    def isLeaf(self):
        if len(self.children) > 0:
            return False
        return True