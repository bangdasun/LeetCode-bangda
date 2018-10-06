class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        mid = n // 2
        for i in range(mid):
            left = s[i]
            right = s[n - i - 1]
            if left != right:
                return False
        return True
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s[(i + 1):(j + 1)]) or self.isPalindrome(s[i:j])
            i += 1
            j -= 1
            
        return True