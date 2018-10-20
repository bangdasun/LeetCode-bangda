class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k == 0:
            nums = nums[:]
        else:
            t = k // n + 1
            nums_extend = nums[:]
            for i in range(t):
                nums_extend = nums + nums_extend

            ans = nums_extend[(-k - n):-k]
            for i in range(n):
                nums[i] = ans[i]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ans = nums[:]
        n = len(nums)
        for i in range(n):
            ans[(i + k) % n] = nums[i]
            
        for i in range(n):
            nums[i] = ans[i]