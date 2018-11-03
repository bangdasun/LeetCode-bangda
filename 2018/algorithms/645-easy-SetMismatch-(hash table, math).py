class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        num_set = set(nums)
        set_sum = sum(num_set)
        arr_sum = sum(nums)
        total_sum = (n + 1) * n / 2
        output = []
        output.append(arr_sum - set_sum)
        output.append(total_sum - set_sum)
        return output
		
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dct = {}
        output = []
        
        for val in nums:
            if dct.get(val, 0) == 0:
                dct[val] = 1
            else:
                output.append(val)
                
        for val in nums:
            new_idx = abs(val) - 1
            nums[new_idx] = abs(nums[new_idx]) * (-1)
        
        for idx, val in enumerate(nums):
            if val > 0:
                output.append(idx + 1)
                break
        
        return output