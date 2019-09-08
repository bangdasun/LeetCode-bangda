# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
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
		
# DFS - inorder traverse + extra space
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

# DFS - inorder traverse + no extra space
class Solution:
    def inorderTraverse(self, root, k):
        if root is None:
            return None
        
        self.inorderTraverse(root.left, k)
        self.index += 1
        if self.index == k:
            self.kth = root.val
            
        if self.index < k:
            self.inorderTraverse(root.right, k)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return None
        
        self.index = 0
        self.kth = root.val
        self.inorderTraverse(root, k)
        return self.kth
