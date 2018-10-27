class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        curr_max = 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                cnt = 0
            
            curr_max = max(cnt, curr_max)
        
        return curr_max