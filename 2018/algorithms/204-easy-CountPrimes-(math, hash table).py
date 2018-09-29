# array
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        isPrime = [True] * n
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                
				# remove all x  to be j (integer) times of i
                for j in range(2, n):
                    if i * j < n:
                        isPrime[i * j] = False
                    else:
                        break
        return count