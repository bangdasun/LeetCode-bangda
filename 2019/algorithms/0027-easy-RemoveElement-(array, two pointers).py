class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast = 0, 0
        n = len(nums)
        
        while fast < n:
            if nums[fast] != val:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                slow += 1
            fast += 1
        
        return slow
