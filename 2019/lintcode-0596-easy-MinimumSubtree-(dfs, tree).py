# recursion
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys

# with global variable
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        self.minimum = sys.maxsize
        self.subtree = None
        self.calcSum(root)
        
        return self.subtree
        
    def calcSum(self, root):
        if root is None:
            return 0
        
        # divide & conquer
        left_sum = self.calcSum(root.left)
        right_sum = self.calcSum(root.right)
        tree_sum = left_sum + right_sum + root.val
        
        # update (traversal)
        if tree_sum < self.minimum:
            self.subtree = root
            self.minimum = tree_sum
        
        return tree_sum

# without global variable
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        minimum, subtree, total_sum = self.getMinSum(root)
        return subtree
        
        
    def getMinSum(self, root):
        """ Return min_sum in root, min_subtree in root, root_sum """
        if root is None:
            return sys.maxsize, None, 0
        
        # divide & conquer
        left_min, left_subtree, left_sum = self.getMinSum(root.left)
        right_min, right_subtree, right_sum = self.getMinSum(root.right)
        total_sum = left_sum + right_sum + root.val
        
        # if min subtree in left
        if left_min == min(left_min, right_min, total_sum):
            return left_min, left_subtree, total_sum
        # if min subtree in right
        if right_min == min(left_min, right_min, total_sum):
            return right_min, right_subtree, total_sum
        
        return total_sum, root, total_sum
