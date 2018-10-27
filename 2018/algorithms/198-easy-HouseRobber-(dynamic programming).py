class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return sum(nums)
        
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
        
        return money[-1]