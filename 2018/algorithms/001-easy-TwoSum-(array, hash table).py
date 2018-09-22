class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        dct = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dct.keys():
                # index of diff
                output.append(dct[diff])
				
                # index of n
                output.append(i)
				
                # assume there is only solution group
                break
            
            # in case there is collision
            dct[n] = i 
                
        return output