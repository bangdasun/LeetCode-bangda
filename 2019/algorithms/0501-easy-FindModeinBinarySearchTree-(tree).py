# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root: TreeNode, path: List[int]):
        if root is None:
            return None
        
        self.dfs(root.left, path)
        path.append(root.val)
        self.dfs(root.right, path)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        
        path = []
        self.dfs(root, path)
        
        num_count = {}
        max_count = 0
        
        for num in path:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
            
            if num_count[num] > max_count:
                max_count = num_count[num]
        
        output = []
        for num, count in num_count.items():
            if count == max_count:
                output.append(num)
        
        return output