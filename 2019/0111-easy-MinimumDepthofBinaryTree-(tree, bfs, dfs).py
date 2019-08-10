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
        
        # define a queue for BFS
        queue = []
        queue.append(root)
        min_depth = 1
        
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                # whether the node is leaf or not
                if node.left is None and node.right is None:
                    return min_depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            min_depth += 1
                
        return min_depth
