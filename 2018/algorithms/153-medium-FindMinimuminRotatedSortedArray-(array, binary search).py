class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if pivot = 0
        if nums[-1] >= nums[0]:
            return nums[0]
        
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[0]:
                return nums[i]
 
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if pivot = 0
        if nums[-1] >= nums[0]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[0]:
                right = mid - 1
				
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if pivot = 0
        if nums[-1] >= nums[0]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                right = mid
            else:
                break
        
        return nums[right]