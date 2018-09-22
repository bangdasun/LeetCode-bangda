class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if n == 0:
            return digits
        
        num = 0
        output = []
        for i in range(n):
            num += digits[i] * 10 ** (n - i - 1)
        
        num += 1
        
        # end with 9, length += 1
        n = len(str(num))
        for i in range(n):
            d = (num // 10 ** (n - i - 1)) % 10
            output.append(d)
        
        return output