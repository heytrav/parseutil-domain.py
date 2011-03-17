'''
Created on Mar 16, 2011

@author: holton
'''

class CondensedRegex(object):
    '''
    CondensedRegex - Take a set of characters and return a tree-like regex
    '''


    def __init__(self):
        '''
        CondensedRegex()
        '''
        
        self.characterStack = {}
        self.maxLength = 0
    
    def add(self, characters):
        self.characterStack.