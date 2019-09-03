# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            level_output = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_output.append(None)
            
            idx = []
            for i in range(len(level_output)):
                if level_output[i] == x or level_output[i] == y:
                    idx.append(i)
            
            if len(idx) == 2:
                if idx[0] % 2 == 1 and idx[1] % 2 == 0:
                    return True
                if idx[1] - idx[0] > 1:
                    return True
        
        return False
