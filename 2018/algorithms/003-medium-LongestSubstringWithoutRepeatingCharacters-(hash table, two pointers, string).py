# brute force - TLE
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                sub_string = s[i:(j + 1)]
                num_unique_string = len(list(set(sub_string)))
                
                # if number of unique string equal to length, it's good
                if num_unique_string == len(sub_string):
                    max_len = max(max_len, num_unique_string)
                
        return max_len

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        slow, fast = 0, 0
        
        # sliding hash table
        dct = {}
        while slow < n and fast < n:
            if s[fast] not in dct.keys():
                dct[s[fast]] = fast
                fast += 1
                max_len = max(max_len, fast - slow)
            else:
                del dct[s[slow]]
                slow += 1
        
        return max_len