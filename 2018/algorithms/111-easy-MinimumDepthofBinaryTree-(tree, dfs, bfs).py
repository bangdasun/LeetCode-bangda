# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
		
		# if only one leaf for the root, should count 2 rather than 1
        if left_depth == 0 or right_depth == 0:
            return max(left_depth, right_depth) + 1
        else:
            return min(left_depth, right_depth) + 1
