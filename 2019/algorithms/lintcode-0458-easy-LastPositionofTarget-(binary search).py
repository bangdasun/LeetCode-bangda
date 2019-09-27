class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
