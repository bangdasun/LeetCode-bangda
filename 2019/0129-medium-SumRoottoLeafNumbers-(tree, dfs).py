# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, path):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            path_sum = int(''.join(path))
            self.output += path_sum
        
        if root.left is not None:
            path.append(str(root.left.val))
            self.dfs(root.left, path)
            path.pop()
        
        if root.right is not None:
            path.append(str(root.right.val))
            self.dfs(root.right, path)
            path.pop()
        
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        path = [str(root.val)]
        self.output = 0
        self.dfs(root, path)
        return self.output
