# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# traversal
class Solution:
    def dfs(self, root, path, target):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            path_sum = sum(path)
            if path_sum == target:
                self.output = True
                return
        
        if root.left is not None:
            path.append(root.left.val)
            self.dfs(root.left, path, target)
            path.pop()
            
        if root.right is not None:
            path.append(root.right.val)
            self.dfs(root.right, path, target)
            path.pop()
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None:
            return False
        
        path = [root.val]
        self.output = False
        self.dfs(root, path, sum)
        return self.output