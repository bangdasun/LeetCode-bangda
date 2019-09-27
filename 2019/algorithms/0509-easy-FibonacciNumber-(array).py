# append to list (stack)
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        
        hist = []
        hist.extend([0, 1])
        for i in range(1, N):
            hist.append(hist[-1] + hist[-2])
        
        return hist[-1]

# pre allocated array
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        
        hist = [0 for _ in range(N + 1)]
        hist[0] = 0
        hist[1] = 1
        for i in range(2, N + 1):
            hist[i] = hist[i-1] + hist[i-2]
        
        return hist[-1]
    