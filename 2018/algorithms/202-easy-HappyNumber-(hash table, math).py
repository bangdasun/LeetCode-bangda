class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = {}
        ssq = 0
        
        while True:
            str_n = str(n)
            for s in str_n:
                ssq += int(s) ** 2
        
            if ssq in history.keys():
                return False
            else:
                if ssq == 1:
                    return True
                else:
                    history[ssq] = 1
                    n = ssq
                    ssq = 0

# A better way to calculate the sum square of digits
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = {}
        ssq = 0
        
        while True:
            # use math operation rather then string interger conversion
            while n > 0:
                ssq += (n % 10) ** 2
                n = n // 10
            
            if ssq in history.keys():
                return False
            else:
                if ssq == 1:
                    return True
                else:
                    history[ssq] = 1
                    n = ssq
                    ssq = 0
            