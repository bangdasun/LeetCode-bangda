class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        
        # ---, +++
        product_1 = sorted_nums[-3] * sorted_nums[-2] * sorted_nums[-1]
        
        # --+
        product_2 = sorted_nums[0] * sorted_nums[1] * sorted_nums[-1]
        
        # -++: max(product_1, product_2)
        
        return max(product_1, product_2)

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_1 = 1000
        min_2 = 1000
        max_1 = -1000
        max_2 = -1000
        max_3 = -1000
        
        for n in nums:
            if n <= min_1:
                min_2 = min_1
                min_1 = n
            elif n <= min_2:  # n in [min_1, min_2]
                min_2 = n
            
            if n >= max_1:    # n is greater than max_1, max_2, max_3 
                max_3 = max_2
                max_2 = max_1
                max_1 = n
            elif n >= max_2:  # n in [max_1, max_2]
                max_3 = max_2
                max_2 = n
            elif n >= max_3:  # n in [max_2, max_3]
                max_3 = n
        
        # ---, +++
        product_1 = max_3 * max_2 * max_1
        
        # --+
        product_2 = min_1 * min_2 * max_1
        
        # -++: max(product_1, product_2)
        
        return max(product_1, product_2)