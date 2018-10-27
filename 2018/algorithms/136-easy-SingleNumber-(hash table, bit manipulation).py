class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        sum2 = sum(set(nums)) * 2
        return sum2 - sum1