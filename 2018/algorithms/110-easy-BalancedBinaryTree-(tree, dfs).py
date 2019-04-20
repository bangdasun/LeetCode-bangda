# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
		
# O(n) solution
# https://leetcode.com/problems/balanced-binary-tree/discuss/157645/Python-Tree-tm
class Solution(object):
    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1
        
    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1 : return -1          
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1