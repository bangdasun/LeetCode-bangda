class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        curr_max_end = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            curr_max_end = max(curr_max_end + nums[i], nums[i])
            curr_max = max(curr_max, curr_max_end)
            
        return curr_max
		
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        
        return max(nums)