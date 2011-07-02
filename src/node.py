'''
Created on Jun 29, 2011

@author: holton
'''
import unittest

from treefix import node


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNodeComparison(self):
        node1 = node.Node()
        node2 = node.Node()
        node1.addBranch("abcdefghi")
        node1.consolidate()
        node2.addBranch("abcdefghi")
        node2.consolidate()
        self.assertEqual(node1, node2, "Nodes equal.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNodeComparison']
    unittest.main()