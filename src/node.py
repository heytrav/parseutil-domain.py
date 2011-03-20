'''
Created on Mar 16, 2011

@author: holton
'''

import tree

class Node(tree.Tree):
    '''
    classdocs
    '''

    def __init__(self, nodeValue = None):
        '''
        Constructor
        '''
        
        super(Node, self).__init__(nodeValue)
     
    def addBranch(self, newBranch):
        
        # partition the branch
        child, offspring = newBranch[0],newBranch[1:]
        if not self.children.has_key(child):
            childNode = Node(child)
            childNode.parent(self)
            self.children[child] = childNode
        else:
            childNode = self.children[child]
        if len(offspring) > 0:
            childNode.addBranch(offspring)
        
                    
        
    def __str__(self):
        node = self.getNodeValue()
        if node is None:
            return self.endOfPath
        elif node == self.wildcard:
            return self.replaceWildcard
        elif node == self.separator:
            return self.replaceSeparator
        return node
         
               
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
    
    
