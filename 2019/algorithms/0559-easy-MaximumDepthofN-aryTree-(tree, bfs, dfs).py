"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        queue = []
        queue.append(root)
        output = []
        
        while len(queue) > 0:
            level_output = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_output.append(node.val)
                if node.children is not None:
                    for child in node.children:
                        queue.append(child)
                    
            output.append(level_output)
            
        return len(output)
