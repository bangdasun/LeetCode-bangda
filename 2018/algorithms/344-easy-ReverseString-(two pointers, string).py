class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            reverse[right], reverse[left] = reverse[left], reverse[right]
            left += 1
            right -= 1
            
        return ''.join(reverse)