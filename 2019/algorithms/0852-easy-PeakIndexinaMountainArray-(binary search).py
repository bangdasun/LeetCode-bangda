class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # since A.length >= 3
        n = len(A)
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid + 1 == n:
                target = A[-1]
            else:
                target = A[mid + 1]
            
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] > A[end]:
            return start
        
        return end
