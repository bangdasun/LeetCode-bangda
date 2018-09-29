class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_cnt = {}
        for s in magazine:
            if s in letter_cnt.keys():
                letter_cnt[s] += 1
            else:
                letter_cnt[s] = 1
        
        for s in ransomNote:
            if s in letter_cnt.keys():
                if letter_cnt[s] > 0:
                    letter_cnt[s] -= 1
                else:
                    return False
            else:
                return False
            
        return True