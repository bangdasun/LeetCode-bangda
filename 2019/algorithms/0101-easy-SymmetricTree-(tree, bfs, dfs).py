# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # define a queue for BFS
        queue = []
        queue.append(root)
        queue.append(root)
        
        while len(queue) > 0:
            node_left = queue.pop(0)
            node_right = queue.pop(0)
            if node_left is None and node_right is None:
                continue
            if node_left is None or node_right is None:
                return False
            if node_left.val != node_right.val:
                return False
            queue.append(node_left.left)
            queue.append(node_right.right)
            queue.append(node_left.right)
            queue.append(node_right.left)
        
        return True
