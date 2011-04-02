'''
Created on Mar 16, 2011

@author: holton
'''

import tree

class Node(tree.Tree):
    '''
    classdocs
    '''
    nodeKeys = {}
    nodeNumber = 0

    def __init__(self, nodeValue = None):
        '''
        Constructor
        '''
        
        super(Node, self).__init__(nodeValue)
 
     
     
    def addBranch(self, newBranch):
        
        # partition the branch
        child, offspring = newBranch[0], newBranch[1:]
        if not self.children.has_key(child):
            childNode = Node(child)
            childNode.parent(self)
            self.children[child] = childNode
        else:
            childNode = self.children[child]
        if len(offspring) > 0:
            childNode.addBranch(offspring)
        
        
        
    def consolidate(self):
        if self.isLeaf():
            print "Returning leaf" 
            # if we're the end of a leaf, return the value
            return self
        elif len(self.children.keys()) == 1:
            # if there is only one child, prepend ourself to their "value"
            # child may be a leaf, or it could be part of a "stem"
            # First pop it out of our hash
            child, childNode = self.children.popitem()
            
            consolidatedChild = childNode.consolidate()
            if consolidatedChild is not None:
                consolidatedValue = consolidatedChild.__str__()
                newChildNodeString = self.__str__() + consolidatedValue
                print( "Consolidating " + self.__str__() + 
                       " and "   + consolidatedValue + " to " 
                       + newChildNodeString)
                childNode.setNodeValue(newChildNodeString)
            
                return childNode
  
        else:
            newChildren = {}
            for child, childNode in self.children.iteritems():
                print "processing child " + child
                replaceWithNode = childNode.consolidate()
                if replaceWithNode is not None:
                    
                    replacementValue = replaceWithNode.__str__()
                    print "Resetting child node to " + replacementValue
                    newChildren[replacementValue] = replaceWithNode
                    replaceWithNode.storeFlat()
                    self.add(replaceWithNode)
                    # print newChildren
            self.children = newChildren
            return self
                
          
    def storeFlat(self):
        Node.nodeNumber += 1
        self.__thisNodeNumber = Node.nodeNumber
        if not Node.nodeKeys.has_key(self.__str__()):
            Node.nodeKeys[self.__str__()] = [self]
        else:
            Node.nodeKeys[self.__str__()].append(self)
          
        
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
    
    
