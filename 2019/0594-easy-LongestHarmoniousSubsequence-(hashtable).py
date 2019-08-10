class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_unique = list(set(nums))
        nums_count = {}
        
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1
        
        max_len = 0
        for num in nums_unique:
            if num + 1 in nums_count:
                max_len = max(max_len, nums_count[num] + nums_count[num + 1])
            
            if num - 1 in nums_count:
                max_len = max(max_len, nums_count[num] + nums_count[num - 1])
            
        return max_len
