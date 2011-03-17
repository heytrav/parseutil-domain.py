'''
Created on Mar 16, 2011
    
@author: holton
'''

class Leaf(object):
    '''
    classdocs
    '''


    def __init__(self,leafChar, parent = None):
        '''
        Constructor
        '''
        self.leafChar = leafChar
        self.parent = parent
        self.siblings = parent.children
        
        
    def __repr__(self):
        return self.leafChar