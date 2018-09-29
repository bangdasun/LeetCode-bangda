class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        for idx, i in enumerate(s[::-1]):
            # stop at the last non-space position: corner case 'a ', 'a   ', ...
            if i != ' ':
                break
        # no space at end, no need to index        
        if idx == 0: 
            s_list = s.split(' ')
        else:
            s_list = s[:-idx].split(' ')
        
        return len(s_list[-1])
		
# a smarter and more straightforward method
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        l = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                l += 1
            else:
                # if the space is not ending space
                if l > 0:
                    break
                    
        return l