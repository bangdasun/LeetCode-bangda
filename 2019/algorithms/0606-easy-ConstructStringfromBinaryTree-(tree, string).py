# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ''
        
        if t.left is None and t.right is None:
            return str(t.val)
        
        left_out = self.tree2str(t.left)
		# to make sure the string is unique
        if t.right is None:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        
        right_out = self.tree2str(t.right)
        return str(t.val) + '(' + left_out + ')' \
                          + '(' + right_out + ')'
