'''
Created on Jul 29, 2011

@author: holton
'''

from . import  node


class RegexNode(node.Node):
    '''
    RegexNode
    '''


    def __init__(self , replaceChars =  [{".":"\."},{"*":"[^\.]+"}]):
        '''
        RegexNode
        '''
        super(RegexNode,self).__init__()
        
        self.__replaceCharacters = replaceChars
        
        
    
    def regexify(self):