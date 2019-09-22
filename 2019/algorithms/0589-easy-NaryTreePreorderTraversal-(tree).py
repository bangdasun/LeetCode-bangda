"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        output = [root.val]
        for node in root.children:
            output.extend(self.preorder(node))
        
        return output
