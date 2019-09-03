# unlike #31, this problem cannot be solved in O(logN)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        for num in nums:
            if num == target:
                return True
        
        return False
