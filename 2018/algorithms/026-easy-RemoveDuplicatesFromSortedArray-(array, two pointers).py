class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        n = len(nums)
        
        if n == 0:
            return 0
        
        while fast < n:
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
        
        return slow + 1