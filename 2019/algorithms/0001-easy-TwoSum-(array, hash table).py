class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_idx_mapping = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in value_idx_mapping.keys() and value_idx_mapping[diff] != idx:
                return [idx, value_idx_mapping[diff]]
            value_idx_mapping[num] = idx
            
        return None
