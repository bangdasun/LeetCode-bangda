# recursive
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, -n)
        
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        
        if n % 2 == 1:
            return self.myPow(x * x, n // 2) * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, -n)
        
        output = self.myPow(x, n // 2)
            
        if n % 2 == 0:
            return output * output
         
        if n % 2 == 1:
            return output * output * x			

# recursive TLE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, -n)
        
        if n % 2 == 0:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2)
        
        if n % 2 == 1:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2) * x			

# iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        # x^n = (x^(-1))^n
        if n < 0:
            x = 1 / x
            n = -n
            
        output = 1
        current_product = x
        
        while n > 0:
            if n % 2 == 1:
                output = output * current_product
            current_product = current_product * current_product
            n //= 2
        
        return output
