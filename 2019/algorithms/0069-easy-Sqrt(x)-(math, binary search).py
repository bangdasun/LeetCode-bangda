class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            m = (left + right) // 2
            if m * m < x:
                left = m + 1
            elif m * m > x:
                right = m - 1
            else:
                return m
        
        return (left + right) // 2
