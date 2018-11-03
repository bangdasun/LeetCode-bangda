class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct = {}
        for letter in s:
            dct[letter] = dct.get(letter, 0) + 1
        
        for letter in t:
            if letter not in dct.keys():
                return False
            if dct[letter] == 0:
                return False
            else:
                dct[letter] = dct.get(letter, 0) - 1
        
        for letter, cnt in dct.items():
            if cnt > 0:
                return False
        
        return True