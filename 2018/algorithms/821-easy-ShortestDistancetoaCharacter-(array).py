# brute force solution
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        C_pos = []
        for idx, val in enumerate(S):
            if val == C:
                C_pos.append(idx)
        
        n = len(S)
        dist = [n - 1] * n
        for i in range(n):
            for j in C_pos:
                dist[i] = min(abs(j - i), dist[i])
        
        return dist
		
# min array solution
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        prev = float('-inf')
        dist = []
        for idx, val in enumerate(S):
            if val == C:
                prev = idx
            dist.append(idx - prev)
            
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if S[i] == C:
                prev = i
            dist[i] = min(dist[i], prev - i)
        
        return dist
