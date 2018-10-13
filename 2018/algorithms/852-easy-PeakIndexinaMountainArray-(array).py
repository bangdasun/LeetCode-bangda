class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        for i in range(n - 1):
            if A[i + 1] < A[i]:
                break
        
        return i
		
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid + 1] > A[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left