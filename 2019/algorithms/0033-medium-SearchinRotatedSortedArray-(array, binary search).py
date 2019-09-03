class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                if nums[right] < target and nums[right] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if nums[left] > target and nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return mid
        
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        start, end = 0, n - 1
        compare_num = nums[-1]
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > compare_num:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            min_index = start
        else:
            min_index = end
        
        if target <= compare_num:
            new_start, new_end = min_index, n - 1
        else:
            new_start, new_end = 0, min_index
        
        while new_start + 1 < new_end:
            new_mid = (new_start + new_end) // 2
            if nums[new_mid] < target:
                new_start = new_mid
            else:
                new_end = new_mid
        
        if nums[new_start] == target:
            return new_start
        if nums[new_end] == target:
            return new_end
        
        return -1
