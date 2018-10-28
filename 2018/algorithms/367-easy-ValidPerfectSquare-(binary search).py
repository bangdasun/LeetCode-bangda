class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        
        left, right = 0, num // 2
        while left < right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq > num:
                right = mid - 1
            elif sq < num:
                left = mid + 1
            else:
                return True
        
        return False
