class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return None
        
        if n == 1:
            return 0
        
        nums_full = [float('-inf')] + nums[:] + [float('-inf')]
        for i in range(1, n + 1):
            if nums_full[i] > nums_full[i-1] and nums_full[i] > nums_full[i+1]:
                return i - 1
        
        return n - 1
        
# binary search
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return None
        
        if n == 1:
            return 0
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return right