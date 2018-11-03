class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_max = 0
        arg_max = 0
        for idx, val in enumerate(nums):
            if val > nums_max:
                nums_max = val
                arg_max = idx
        
        nums.remove(nums_max)
        if len(nums) > 0:
            other_max = max(nums)
        else:
            other_max = 0
        
        if nums_max >= 2 * other_max:
            return arg_max
        else:
            return -1
			
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_max = 0
        arg_max = 0
        for idx, val in enumerate(nums):
            if val > nums_max:
                nums_max = val
                arg_max = idx
        
        for val in nums:
            if nums_max < 2 * val and nums_max != val:
                return -1
        
        return arg_max