class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        n_A = len(A)
        n_B = len(B)
        if n_A != n_B:
            return False
        
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
                
            return False
        else:
            pairs = []
            for i in range(n_A):
                if A[i] != B[i]:
                    pairs.append([A[i], B[i]])
            
            if len(pairs) != 2:
                return False
            else:
                return pairs[0] == pairs[1][::-1]