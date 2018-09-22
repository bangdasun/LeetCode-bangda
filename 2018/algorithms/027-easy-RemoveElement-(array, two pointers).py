class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        
        i, j = -1, 0
        while j < n:
            if nums[j] != val:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
            
        return i + 1