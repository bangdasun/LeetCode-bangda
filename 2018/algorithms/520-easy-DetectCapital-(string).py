class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        count_upper = 0
        for s in word:
            if s.isupper():
                count_upper += 1
        
        if count_upper == n or count_upper == 0:
            return True
        elif count_upper == 1:
            return word[0].isupper()
        else:
            return False