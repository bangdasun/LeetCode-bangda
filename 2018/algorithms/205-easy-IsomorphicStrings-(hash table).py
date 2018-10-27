class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct = {}
        for idx, val in enumerate(s):
            if val in dct.keys():
                if dct[val] != t[idx]:
                    return False
            else:
                if t[idx] in dct.values():
                    return False
                dct[val] = t[idx]
            
        return True

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct_s2t = {}
        dct_t2s = {}
        for idx, val in enumerate(s):
            if val in dct_s2t.keys():
                if dct_s2t[val] != t[idx]:
                    return False
            else:
                dct_s2t[val] = t[idx]
            
            if t[idx] in dct_t2s.keys():
                if dct_t2s[t[idx]] != val:
                    return False
            else:
                dct_t2s[t[idx]] = val
            
        return True