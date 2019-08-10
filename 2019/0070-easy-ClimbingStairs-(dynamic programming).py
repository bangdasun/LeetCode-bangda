class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        output = []
        output.append(1)
        output.append(2)
        
        for i in range(2, n):
            steps = output[-1] + output[-2]
            output.append(steps)
        
        return output[-1]
