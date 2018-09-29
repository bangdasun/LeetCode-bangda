class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_num = sum(nums)
        n = len(nums)
            
        return int(n * (n + 1) / 2 - sum_num)