class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        n = len(S)
        i, j = 0, 0
        output = []
        
        while j < n:
            if S[i] == S[j]:
                j += 1
            else:
                diff = j - i
                if diff >= 3:
                    output.append([i, j - 1])
                i = j
				
        # corner case: 'aaa' at end
        if S[i] == S[j - 1] and j - i >= 3:
            output.append([i, j - 1])
            
        return output