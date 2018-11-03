# TLE
class Solution(object):
    def isSquare(self, c):
        if c < 2:
            return True
        
        left, right = 0, c // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == c:
                return True
            elif mid * mid > c:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c <= 1:
            return True
        
        a = 0
        while a * a < c:
            b_sq = c - a * a
            if self.isSquare(b_sq):
                return True
            a += 1
            
        return False

# Fermat theorem
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 2
        while a * a < c:
            count = 0
            if c % a == 0:
                while c % a == 0:
                    count += 1
                    c = c / a
                
                if a % 4 == 3 and count % 2 != 0:
                    return False
            
            a += 1
        
        return c % 4 != 3