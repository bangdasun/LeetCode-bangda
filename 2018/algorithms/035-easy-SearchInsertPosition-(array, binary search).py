class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
            
        if nums[m] > target:
            return m
        else:
            return m + 1