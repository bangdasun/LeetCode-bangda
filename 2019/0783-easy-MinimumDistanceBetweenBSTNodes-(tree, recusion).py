# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# inorder traversal - recursion
class Solution:
    def dfs(self, root, path):
        if root is None:
            return None
        
        self.dfs(root.left, path)
        path.append(root.val)
        self.dfs(root.right, path)
    
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
            
        minimum = sys.maxsize
        path = []
        self.dfs(root, path)
        
        for i in range(len(path) - 1):
            if path[i+1] - path[i] < minimum:
                minimum = path[i+1] - path[i]
        
        return minimum