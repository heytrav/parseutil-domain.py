'''
Created on Jul 29, 2011

@author: holton
'''

from . import  node


class RegexNode(node.Node):
    '''
    RegexNode
    '''


    def __init__(self , 
                 nodeValue = None,
                 wildcard = None, 
                 replaceWildcard = None, 
                 separator = None,
                 replaceSeparator = None,
                 applyCompression = None,
                 escapeChars = None,
                 endOfPath = "",
                 replaceChars =  [{".":"\."},{"*":"[^\.]+"}]
                 ):
        '''
        RegexNode
        '''
        super(RegexNode,self).__init__(  
                                       nodeValue ,  
                                       wildcard ,  
                                       replaceWildcard,    
                                       separator ,
                                       replaceSeparator ,  
                                       applyCompression , 
                                       escapeChars ,
                                       endOfPath ,
                                       )
        
        self.__replaceCharacters = replaceChars
        
        
    
    def regexify(self):
        def recursiveRegexify(data):
            if isinstance(data, dict):
                iter = data.iteritems()
                k, childNodes = iter.next()
                joinedString = "|".join([self.recursiveRegexify(i) for i in childNodes])
        
                return self.replaceCharacters(k) + "(?:" + joinedString + ")"
            elif isinstance(data, str):
                return self.replaceCharacters(data) 
        consolidated = self.consolidate()
        regexed = recursiveRegexify(consolidated.getSubDataStructure())     
        return regexed
         
         
         
    def replaceCharacters(self,data):
        if self.__replaceCharacters is not None:
            for element in self.__replaceCharacters:
                replKeys = element.keys()
                for replKey in replKeys:
                    val = element.get(replKey)
                    newString = data.replace(replKey, val)
                    data = newString
      
        return data
    