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

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        start, end = 0, x - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid < x:
                start = mid
            elif mid * mid == x:
                end = mid
            else:
                end = mid
        
        if end * end <= x:
            return end
        
        return start
