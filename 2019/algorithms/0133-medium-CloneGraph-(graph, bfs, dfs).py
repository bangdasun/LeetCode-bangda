"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

from collections import deque

class Solution:
    def getNodes(self, node: 'Node'):
        queue = deque([node])
        visited = set([node])
        while len(queue) > 0:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # G = (E, V)
        # 1. copy nodes
        # 2. copy edges
        root = node
        all_nodes = self.getNodes(root)
        
        # create a mapping from old nodes to new nodes
        old_to_new = {}
        
        # copy nodes
        for node in all_nodes:
            old_to_new[node] = Node(val=node.val, neighbors=[])
        
        # copy edges
        for node in all_nodes:
            new_node = old_to_new[node]
            for neighbor in node.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return old_to_new[root]
        