class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        
        hist = []
        hist.extend([0, 1])
        for i in range(1, N):
            hist.append(hist[-1] + hist[-2])
        
        return hist[-1]
