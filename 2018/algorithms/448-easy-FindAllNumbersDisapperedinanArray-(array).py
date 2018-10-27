class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for val in nums:
            new_idx = abs(val) - 1
            nums[new_idx] = abs(nums[new_idx]) * (-1)
        
        output = []
        for i in range(n):
            if nums[i] > 0:
                output.append(i + 1)
        
        return output