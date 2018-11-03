class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        divisor_sum = 0
        for i in range(1, num):
            if i * i > num:
                break
                
            if num % i == 0:
                divisor_sum += i
                if i * i != num:
                    divisor_sum += num / i
        
        return divisor_sum - num == num

# Euclid-Euler theorem
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        primes = [2, 3, 5, 7, 13, 17, 19, 31]
        for i in primes:
            if 2 ** (i - 1) * (2 ** i - 1) == num:
                return True
        
        return False