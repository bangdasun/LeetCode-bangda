class Solution:
    def searchFirst(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
        
    def searchLast(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_loc = self.searchFirst(nums, target)
        last_loc = self.searchLast(nums, target)
        return [first_loc, last_loc]
    