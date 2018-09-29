class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = {}
        
        for idx, val in enumerate(nums):
            if val in dct.keys():
                diff = idx - dct[val]
                dct[val] = idx
                if diff <= k:
                    return True
            else:
                dct[val] = idx
        
        return False