# TLE solution
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        avg = (sum_A + sum_B) / 2
        
        dct = {}
        for i in A:
            dct[avg + i - sum_A] = i
        
        for i in B:
            if i in dct.keys():
                return [dct[i], i]
				
# AC solution
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        set_B = set(B)
        
        for x in A:
            y = x + (sum_B - sum_A) / 2
            if y in set_B:
                return [x, y]