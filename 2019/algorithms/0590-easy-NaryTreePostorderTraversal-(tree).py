"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        output = []
        for node in root.children:
            output.extend(self.postorder(node))
        output.append(root.val)
        
        return output
