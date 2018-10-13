class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        sol = [0] * n
        sol[0] = 1
        sol[1] = 2
        
        for i in range(2, n):
            sol[i] = sol[i - 1] + sol[i - 2]
            
        return sol[-1]