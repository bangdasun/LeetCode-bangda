# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root: TreeNode):
        if root is None:
            return None
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # reconstruct two chains
		#   root
		# /      \
		# \       \
		#  \       \
		#   \       \
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        # look at right first
        if right_last is not None:
            return right_last
        
        if left_last is not None:
            return left_last
        
        return root
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        self.helper(root)
