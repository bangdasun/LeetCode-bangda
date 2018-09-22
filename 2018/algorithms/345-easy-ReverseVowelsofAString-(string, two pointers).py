class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        i, j = 0, n - 1
        
        if j <= 0:
            return s
        
        s_list = list(s)
        
        while i < j:
            if s_list[i] in vowels:
                if s_list[j] in vowels:
                    s_list[j], s_list[i] = s_list[i], s_list[j]
                    i += 1
                j -= 1
            else:
                if s_list[j] in vowels:
                    i += 1
                else:
                    j -= 1
                
        return ''.join(s_list)