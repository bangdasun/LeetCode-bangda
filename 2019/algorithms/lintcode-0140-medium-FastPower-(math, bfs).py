# TLE solution
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        current_product = a
        a_power_n = 1
        while n > 0:
            if n % 2 == 1:
                a_power_n = a_power_n * current_product
                n -= 1
            else:
                current_product = current_product * current_product
                n //= 2
        
        slow, fast = 0, 0
        while b * fast < a_power_n:
            slow = fast
            fast = 2 ** (fast + 1) - 1
            
        while slow + 1 < fast:
            mid = (slow + fast) // 2
            if b * mid < a_power_n:
                slow = mid
            elif b * mid == a_power_n:
                return 0
            else:
                fast = mid
        
        if a_power_n > b:
            return a_power_n - b * slow
        if a_power_n == b:
            return 0
        
        return a_power_n
		
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b
