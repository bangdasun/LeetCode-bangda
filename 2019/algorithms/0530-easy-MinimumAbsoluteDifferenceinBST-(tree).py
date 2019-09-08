# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

# inorder traversal - recursion
class Solution:
    def dfs(self, root):
        if root is None:
            return []
        
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return None
        
        path = self.dfs(root)
        minimum = sys.maxsize
        for i in range(len(path) - 1):
            if path[i+1] - path[i] < minimum:
                minimum = path[i+1] - path[i]
        
        return minimum
