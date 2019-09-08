# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root, path):
        if root is None:
            return None
        
        self.inorder(root.left, path)
        path.append(root.val)
        self.inorder(root.right, path)
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
            
        path = []
        self.inorder(root, path)
        
        n = len(path)
        for i in range(n-1):
            if path[i] >= path[i+1]:
                return False
        
        return True
    