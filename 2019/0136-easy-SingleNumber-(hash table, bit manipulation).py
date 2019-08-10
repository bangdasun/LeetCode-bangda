class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        
        for num in nums:
            if dct[num] == 1:
                return num
        
        return None
		

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dct = {}
        for num in nums:
            if num in dct:
                dct.pop(num)
            else:
                dct[num] = 1
        
        return dct.popitem()[0]
