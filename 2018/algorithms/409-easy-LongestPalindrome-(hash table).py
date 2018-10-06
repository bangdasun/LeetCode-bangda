class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for i in s:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        
        length = 0
        add_one = False
        add_odd = False
        for k, v in dct.items():
            if v % 2 == 1:
                if v == 1:
                    add_one = True
                elif v > 1:
                    add_odd = True
                dct[k] -= 1
            
            length += dct[k]
        
        if add_one or add_odd:
            length += 1
        
        return length
		
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for i in s:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        
        length = 0
        for k, v in dct.items():
            length += (dct[k] // 2) * 2
            if dct[k] % 2 == 1 and length % 2 == 0:
                length += 1
        
        return length 