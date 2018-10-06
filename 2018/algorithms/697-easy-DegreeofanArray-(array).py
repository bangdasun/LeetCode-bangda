class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, dct = {}, {}, {}
        for idx, val in enumerate(nums):
            if val not in slow:
                slow[val] = idx
            
            fast[val] = idx
            dct[val] = dct.get(val, 0) + 1
        
        deg = max(dct.values())
        curr_min = len(nums)
        for k, v in dct.items():
            if deg == v:
                curr_min = min(curr_min, fast[k] - slow[k] + 1)
                
        return curr_min