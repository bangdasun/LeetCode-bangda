class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid + 1 > n:
                break
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return end
        if nums[start] > nums[end]:
            return start
