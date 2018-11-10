class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for idx, val in enumerate(nums):
            new_idx = abs(val) - 1
            if nums[new_idx] > 0:
                nums[new_idx] = -nums[new_idx]
            else:
                output.append(new_idx + 1)
        
        return output