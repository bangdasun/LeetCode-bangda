class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_h = len(haystack)
        n_n = len(needle)
        
        if n_n == 0:
            return 0
        elif n_h == 0: 
            # when needle not empty but haystack empty
            return -1
        
        slow, fast = 0, 0
        while slow < n_h and fast < n_n:
            if haystack[slow] == needle[fast]:
                fast += 1
            else:
                slow -= fast # if no match, slow should back to initial compare position
                fast = 0
            slow += 1
        
        # if the fast at end+1: last fast also has a match
        if fast == n_n:
            return fast - slow
        
        # if j is still in needle range (then must be i at end+1) and if last ith val != to current j: no match
        # exception case: last ith val == current j: haystack = 'aaa' needle = 'aaaa' (fixed by slow -= fast)
        if fast <= (n_n - 1):
            return -1