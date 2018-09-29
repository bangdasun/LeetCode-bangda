# brute force
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        n = len(strs)
        if n == 0:
            return ""
        
        if n == 1:
            return strs[0]
        
        min_len = len(strs[0])
        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)
        
        pos = 0
        common_prefix = ""
        
        while pos < min_len:
            curr = strs[0][pos]
            print(pos, curr, common_prefix)
            for s in strs[1:]:
                if s[pos] != curr:
                    return common_prefix
            
            common_prefix += curr
            pos += 1
        
        return common_prefix
		
# horizontal scanning
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        n = len(strs)
        if n == 0:
            return ""
        
        if n == 1:
            return strs[0]
        
        common_prefix = strs[0]
        for s in strs[1:]:
            min_len = min(len(common_prefix), len(s))
            
            # if empty string exists: ["", "any"], ["any", ""]
            if min_len == 0:
                return ""
            
            for i in range(min_len):
                if common_prefix[i] != s[i]:
                    break
                    
            if common_prefix[i] == s[i]:
                common_prefix = s[:(i + 1)]
            else:
                common_prefix = s[:i]
            
        return common_prefix