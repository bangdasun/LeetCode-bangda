class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        cnt = 1
        A_extend = A
        
        while len(A_extend) < 2 * len(B):
            if B in A_extend:
                return cnt
            
            A_extend += A
            cnt += 1
        
        if B in A_extend:
            return cnt
        
        if B in A_extend + A:
            return cnt + 1
        
        return -1
		
# more smart solution
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = (len(B) - 1) // len(A) + 1
        
        for i in range(2):
            if B in A * (q + i): return q + i
            
        return -1