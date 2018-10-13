class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        montonic = [0] * (n - 1)
        non_zero = 0
        for i in range(n - 1):
            if A[i + 1] > A[i]:
                montonic[i] = 1
                non_zero += 1
            elif A[i + 1] < A[i]:
                montonic[i] = -1
                non_zero += 1
            else:
                montonic[i] = 0
            
        all_sum = abs(sum(montonic))
        return non_zero == all_sum
		
# more space saving solution
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        increase = decrease = True
        for i in range(n - 1):
            if A[i + 1] > A[i]:
                decrease = False
            elif A[i + 1] < A[i]:
                increase = False
                
        return increase or decrease