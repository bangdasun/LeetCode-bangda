# sliding window
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n == k:
            return sum(nums) / float(k)
        
        curr_max = sum(nums[:k])
        curr_sum = curr_max
        for i in range(k, n):
            curr_max += nums[i] - nums[i - k]
            curr_sum = max(curr_max, curr_sum)
            
        return curr_sum / float(k)

# cumulative sum
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n == k:
            return sum(nums) / float(k)
        
        cumsum = nums[:]
        for idx in range(1, n):
            cumsum[idx] = cumsum[idx - 1] + nums[idx]
        
		# start from [-1]
        curr_max = cumsum[k - 1] 
        for i in range(k, n):
            curr_max = max(curr_max, cumsum[i] - cumsum[i - k])
            
        return curr_max / float(k)