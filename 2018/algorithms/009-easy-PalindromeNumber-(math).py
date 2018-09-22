class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        n = len(str_x)
        mid = int(n / 2)
        output = True
        
        i = 0
        while i < mid:
            left = str_x[i]
            right = str_x[n - i - 1]
            if left != right:
                output = False
                break
            i += 1
            
        return output