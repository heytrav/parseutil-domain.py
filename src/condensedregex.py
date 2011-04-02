'''
Created on Mar 16, 2011

@author: holton
'''

class CondensedRegex(object):
    '''
    CondensedRegex - Take a set of characters and return a tree-like regex
    '''


    def __init__(self, node):
        '''
        CondensedRegex()
        '''
        
        self.__node = node
    
