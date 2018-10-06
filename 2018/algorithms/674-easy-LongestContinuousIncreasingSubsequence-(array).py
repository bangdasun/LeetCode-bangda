class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        n = len(nums)
        if n == 0:
            return 0
        
        cnt = 1
        curr_max = 1
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 0:
                cnt += 1
            else:
                cnt = 1
            curr_max = max(curr_max, cnt)
            
        return curr_max
		
# use anchor to mark the descending start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        n = len(nums)
        if n == 0:
            return 0
        
        anchor = 0
        curr_max = 0
        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] <= 0:
                anchor = i
            
			# object array is from nums[anchor] to nums[i]
            curr_max = max(curr_max, i - anchor + 1)
            
        return curr_max