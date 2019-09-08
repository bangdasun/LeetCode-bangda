# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, path):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            self.output.extend(path)
        
        if root.left is not None:
            path.append(root.left.val)
            self.dfs(root.left, path)
            path.pop()
        
        if root.right is not None:
            path.append(root.right.val)
            self.dfs(root.right, path)
            path.pop()
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        path = [root.val]
        self.output = []
        self.dfs(root, path)
        
        if len(set(self.output)) == 1:
            return True
        
        if len(set(self.output)) > 1:
            return False
