class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct_cnt = {}
        for l in s:
            if l in dct_cnt.keys():
                dct_cnt[l] += 1
            else:
                dct_cnt[l] = 1
        
        for idx, l in enumerate(s):
            if dct_cnt[l] == 1:
                return idx
            
        return -1