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
