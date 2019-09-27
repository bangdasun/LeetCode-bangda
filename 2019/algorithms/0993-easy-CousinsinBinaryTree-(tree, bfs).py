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

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        
        queue = deque([root])
        while len(queue) > 0:
            level_output = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is not None:
                    level_output.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_output.append('null')
            
            # find x, y
            target = []
            for i in range(len(level_output)):
                if level_output[i] == str(x) or level_output[i] == str(y):
                    target.append(i)
            
            # x, y not in same level
            if len(target) == 1:
                return False
            
            if len(target) == 2:
                # x, y not adjacent
                if target[1] - target[0] > 1:
                    return True

                # x, y adjacent but not same parent (x in odd and y in even index)
                if target[0] % 2 == 1 and target[1] % 2 == 0:
                    return True
        
        return False
