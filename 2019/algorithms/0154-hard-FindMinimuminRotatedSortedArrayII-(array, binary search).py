# similar with #81, worst case to solve this will be O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return None
        
        min_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
        
        return min_num
