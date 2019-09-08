"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def dfs(self, root, path):
        if root is None:
            return None
        
        self.dfs(root.left, path)
        path.append(root.val)
        self.dfs(root.right, path)

        
    def closestValue(self, root, target):
        if root.left is None and root.right is None:
            return root.val
            
        minimum = sys.maxsize
        path = []
        self.dfs(root, path)
        
        # because path is sorted (inorder traversal of BST)
        left, right = 0, len(path) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if path[mid] < target:
                left = mid
            elif path[mid] == target:
                return path[mid]
            else:
                right = mid
        
        if target - path[left] < path[right] - target:
            return path[left]
        else:
            return path[right]
