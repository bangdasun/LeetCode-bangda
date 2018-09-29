# brute force
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimal_a, decimal_b = 0, 0
        len_a, len_b = len(a), len(b)
        for i in range(len_a):
            decimal_a += int(a[i]) * 2 ** (len_a - i - 1)
        
        for i in range(len_b):
            decimal_b += int(b[i]) * 2 ** (len_b - i - 1)
            
        two_sum = decimal_a + decimal_b
        
        two_sum_binary = ""
        while two_sum > 1:
            two_sum_binary = ''.join([str(two_sum % 2), two_sum_binary])
            two_sum = two_sum // 2
            
        if two_sum <= 1:
            return ''.join([str(two_sum % 2), two_sum_binary])
        
        return two_sum_binary
		
# string addition
# https://leetcode.com/problems/add-binary/discuss/168118/Python-Binary-Addition-Solution
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rev_a, rev_b = a[::-1], b[::-1]
        len_a, len_b = len(a), len(b)
        
        # padding to make sure equal length
        i, j = 0, 0
        while len(rev_a) != len(rev_b):
            if len(rev_a) < len(rev_b):
                rev_a += '0'
            else:
                rev_b += '0'
                
        two_sum_binary = []
        carry = 0
        for i, j in zip(rev_a, rev_b):
            temp = int(i) + int(j) + carry
            
            if temp == 2:
                two_sum_binary.append(0)
                carry = 1
            elif temp < 2:
                two_sum_binary.append(temp)
                carry = 0
            else:
                two_sum_binary.append(1)
                carry = 1
        
        if carry == 1:
            two_sum_binary.append(carry)
        
        return ''.join([str(i) for i in two_sum_binary[::-1]])