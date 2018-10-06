# sorting
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return 0
        
		# iterate might not be executed, therefore start and end have to be initialized
        start, end = 0, 0
        for i in range(n):
            if sorted_nums[i] != nums[i]:
                start = i
                break
            
        for i in range(n):
            if sorted_nums[i] != nums[i]:
                end = i
            
        return end - start + 1 if end > start else 0
