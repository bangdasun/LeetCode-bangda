class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        count_LL = 0
        count_LL_list = []
        n = len(s)
        
        i = 0
        while i < n:
            if s[i] == 'A':
                count_A += 1
            
            if i < n - 1 and s[i] == 'L':
                if s[i + 1] == 'L':
                    count_LL += 2
                else:
                    if count_LL > 0:
                        count_LL_list.append(count_LL)
                    count_LL = 1
                    count_LL_list.append(count_LL)
                    count_LL = 0
            
            i += 1
        
        count_LL_list.append(count_LL)
        
        return count_A <= 1 and max(count_LL_list) <= 2
		
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        has_A = False
        count_L = 0
        
        for l in s:
            if l == 'L':
                count_L += 1
                if count_L > 2:
                    return False
            else:
                count_L = 0
                if l == 'A':
                    if has_A:
                        return False
                    else:
                        has_A = True
        
        return True