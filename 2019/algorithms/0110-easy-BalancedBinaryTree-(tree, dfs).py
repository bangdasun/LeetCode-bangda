# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
