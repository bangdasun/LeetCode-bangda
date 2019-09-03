class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        
        left, right = 1, num // 2
        while left <= right:
            m = (left + right) // 2
            if m * m < num:
                left = m + 1
            elif m * m > num:
                right = m - 1
            else:
                return True
        
        return False
