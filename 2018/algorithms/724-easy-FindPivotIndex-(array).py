class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        left_sum = 0
        for idx, x in enumerate(nums):
            if left_sum == S - left_sum - nums[idx]:
                return idx
            left_sum += x
        
        return -1