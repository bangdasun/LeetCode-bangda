class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for val in nums:
            dct[val] = dct.get(val, 0) + 1
        
        for idx, val in dct.items():
            if val > 1:
                return idx
        
        return -1

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
            
        return -1
		
# https://leetcode.com/problems/find-the-duplicate-number/
# Approach #3 Floyd's Tortoise and Hare (Cycle Detection)