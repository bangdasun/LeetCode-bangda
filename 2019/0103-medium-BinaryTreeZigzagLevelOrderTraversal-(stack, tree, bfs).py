# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if root is None:
            return output
        
        queue = []
        queue.append(root)
        iter_idx = 0
        
        while len(queue) > 0:
            level_output = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_output.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            if iter_idx % 2 == 0:
                output.append(level_output)
            else:
                output.append(level_output[::-1])
            iter_idx += 1
        
        return output
