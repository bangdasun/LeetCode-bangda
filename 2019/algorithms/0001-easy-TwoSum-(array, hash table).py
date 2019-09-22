# one pass
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index and index != num_to_index[diff]:
                return [index, num_to_index[diff]]
            num_to_index[num] = index
        
        return None
		
# two pass (more clear)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        
        for index, num in enumerate(nums):
            num_to_index[num] = index
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff not in num_to_index:
                continue
            if diff == num and index == num_to_index[diff]:
                continue
            
            return [index, num_to_index[diff]]
        
        return None