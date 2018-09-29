class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # corner case: int(x/2) = 0 if x in [1, 2)
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            m = (left + right) // 2
            if m * m < x:
                # start from middle
                left = m + 1
            elif m * m > x:
                # start from middle
                right = m - 1
            else:
                return m
        
        if m * m > x:
            return m - 1
        else:
            return m