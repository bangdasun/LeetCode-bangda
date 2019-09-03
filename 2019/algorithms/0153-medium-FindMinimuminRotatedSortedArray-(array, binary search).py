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

		
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        
        n = len(nums)
        if n == 0:
            return None
        
        start, end = 0, n - 1
        
        # find the first position less than target
        target = nums[-1] 
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
