class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_array = s.split(' ')
        for idx, w in enumerate(word_array):
            word_array[idx] = w[::-1]
        
        return ' '.join(word_array)