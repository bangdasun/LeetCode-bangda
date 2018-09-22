class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
        i, j = 0, len(s) - 1
        ans = False
        while i < j:
            if s[i].lower() != s[j].lower():
                # skip non-alphanumeric letters
                if s[i].lower() not in alphanumeric:
                    i += 1
                    continue
                if s[j].lower() not in alphanumeric:
                    j -= 1
                    continue
                
                # unequal alphanumeric
                if s[i].lower() in alphanumeric and s[j].lower() in alphanumeric:
                    return False
            else:
                ans = True
                i += 1
                j -= 1
        
        # in case of 'a.'
        if i == j:
            ans = True
        
        return ans # after AC: could just return True, since the only False case will be returned immediately