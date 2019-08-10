class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        
        s_count = {}
        for char in s:
            if char not in s_count:
                s_count[char] = 1
            else:
                s_count[char] += 1
        
        for char in t:
            if char not in s_count:
                return False
            else:
                if s_count[char] < 0:
                    return False
                s_count[char] -= 1
        
        for char, count in s_count.items():
            if count > 0:
                return False
        
        return True
