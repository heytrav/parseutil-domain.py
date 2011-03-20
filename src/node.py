'''
Created on Mar 16, 2011

@author: holton
'''

import tree

class Node(tree.Tree):
    '''
    classdocs
    '''

    def __init__(self, nodeValue):
        '''
        Constructor
        '''
        
        super(Node).__init__(nodeValue)
     
    def addBranch(self, newBranch):
        child, offspring = newBranch[0],newBranch[1:]
        childNode = Node(child)
        if not self.children.has_key(child):
            self.children[child] = [childNode]
        else:
            self.children[child].append(childNode)
        
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
    
    
