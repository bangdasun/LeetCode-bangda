"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        queue = deque([root])
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)    
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
            for i in range(len(level) - 1):
                node_prev = level[i]
                node_next = level[i+1]
                node_prev.next = node_next
        
        return root
