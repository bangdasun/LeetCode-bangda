# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = []
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    output.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        return sorted(output)[k-1]
		

class Solution:
    def inorderTraverse(self, root):
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        return self.inorderTraverse(root.left) + [root.val] + self.inorderTraverse(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = self.inorderTraverse(root)
        return output[k-1]
