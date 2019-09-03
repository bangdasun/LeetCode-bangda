"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        if root is None:
            return output
        
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            level_output = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_output.append(node.val)
                for j in range(len(node.children)):
                    child = node.children.pop(0)
                    queue.append(child)
            output.append(level_output)
        
        return output
