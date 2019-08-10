class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count = {}
        n = len(s)
        
        if n == 0:
            return -1
        
        if n == 1:
            return 0
        
        for char in s:
            if char not in s_count:
                s_count[char] = 1
            else:
                s_count[char] += 1
        
        for idx, char in enumerate(s):
            if s_count[char] == 1:
                return idx
        
        return -1
