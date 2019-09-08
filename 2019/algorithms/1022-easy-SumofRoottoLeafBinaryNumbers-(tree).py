# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binary_to_decimal(self, num):
        n = len(num)
        output = 0
        for i in range(n):
            output += int(num[i]) * 2 ** int(n-i-1)
            
        return output
        
    def dfs(self, root, path):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            self.output.append(''.join(path))
        
        if root.left is not None:
            path.append(str(root.left.val))
            self.dfs(root.left, path)
            path.pop()
        
        if root.right is not None:
            path.append(str(root.right.val))
            self.dfs(root.right, path)
            path.pop()
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        path = [str(root.val)]
        self.output = []
        self.dfs(root, path)
        num_sum = 0
        
        for num in self.output:
            num_sum += self.binary_to_decimal(num)
        
        return num_sum
