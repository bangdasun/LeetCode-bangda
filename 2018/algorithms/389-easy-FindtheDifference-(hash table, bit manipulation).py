class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dct = {}
        for i in s:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        
        for i in t:
            if i not in dct.keys():
                return i
            else:
                if dct[i] > 0:
                    dct[i] -= 1
                else:
                    return i