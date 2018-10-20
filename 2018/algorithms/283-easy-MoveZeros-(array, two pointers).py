# brute force
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for idx, val in enumerate(nums):
            if val == 0:
                for j in range(idx, len(nums)):
                    if nums[j] != 0:
                        nums[j], nums[idx] = nums[idx], nums[j]
                        break
						
# public solution 1
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIdx = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIdx] = nums[i]
                lastNonZeroIdx += 1
        
        for i in range(lastNonZeroIdx, len(nums)):
            nums[i] = 0

# public solution 2
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIdx = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] != 0:
                nums[lastNonZeroIdx], nums[idx] = nums[idx], nums[lastNonZeroIdx]
                lastNonZeroIdx += 1
            idx += 1