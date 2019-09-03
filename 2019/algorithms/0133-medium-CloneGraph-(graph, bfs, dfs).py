"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

from collections import deque

class Solution:
    def getNodes(self, node: 'Node') -> list:
        """ Get all nodes in the graph from start node using BFS """
        queue = deque([node])
        visited = set([node])
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor is None or neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
                
        return list(visited)
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        
        root = node
        all_nodes = self.getNodes(root)
        
        # mapping from old nodes to new nodes
        mapping = {}
        
        # copy nodes
        for node in all_nodes:
            new_node = Node(val=node.val, neighbors=[])
            mapping[node] = new_node
        
        # copy edges
        for node in all_nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]
