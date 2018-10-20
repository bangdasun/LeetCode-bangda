# hash table
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dct = {}
        for i in nums:
            if dct.get(i, 0) > 0:
                return True
            else:
                dct[i] = 1
                
        return False