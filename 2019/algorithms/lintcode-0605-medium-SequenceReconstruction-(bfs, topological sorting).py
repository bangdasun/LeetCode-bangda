
from collections import deque

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def construct_graph(self, seqs):
        nodes = set()
        edges = set()
        
        for seq in seqs:
            if len(seq) == 0:
                continue
            for i in range(len(seq) - 1):
                if seq[i] not in nodes:
                    nodes.add(seq[i])
                if (seq[i], seq[i + 1]) not in edges:
                    edges.add((seq[i], seq[i + 1]))

            if seq[-1] not in nodes:
                nodes.add(seq[-1])
        
        nodes_to_next = {node: [] for node in nodes}
        nodes_to_indegree = {node: 0 for node in nodes}
        
        for edge in edges:
            nodes_to_next[edge[0]].append(edge[1])
            nodes_to_indegree[edge[1]] += 1
        
        return nodes, nodes_to_next, nodes_to_indegree
                
    def sequenceReconstruction(self, org, seqs):
        nodes, nodes_to_next, nodes_to_indegree = self.construct_graph(seqs)
        print(nodes_to_next, nodes_to_indegree)
        queue = deque([node for node in nodes if nodes_to_indegree[node] == 0])
        reconstructed_seq = []
        
        while len(queue) > 0:
            if len(queue) > 1:
                return False
                
            node = queue.popleft()
            reconstructed_seq.append(node)
            for next_node in nodes_to_next[node]:
                print(node, next_node)
                nodes_to_indegree[next_node] -= 1
                if nodes_to_indegree[next_node] == 0:
                    queue.append(next_node)
        
        return reconstructed_seq == org
