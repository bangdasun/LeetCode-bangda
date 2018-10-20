class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_non_space = False
        is_space = False
        cnt = 0
        for i in s:
            if i != ' ':
                if is_space or not is_non_space:
                    is_space = False
                    cnt += 1
                is_non_space = True
            else:
                if is_non_space or not is_space:
                    is_non_space = False
                is_space = True
                    
        return cnt
		
# more clear solution
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                cnt += 1
        
        return cnt