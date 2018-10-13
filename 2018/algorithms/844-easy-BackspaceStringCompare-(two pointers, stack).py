# my stack solution
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        nS = len(S)
        nT = len(T)
        
        stack_S, stack_T = [], []
        
        i, j = 0, 0
        while i < nS and j < nT:
            if S[i] != '#':
                stack_S.append(S[i])
            else:
                if len(stack_S) > 0:
                    out = stack_S.pop()
            
            if T[j] != '#':
                stack_T.append(T[j])
            else:
                if len(stack_T) > 0:
                    out = stack_T.pop()
            
            i += 1
            j += 1
        
        if i < nS:
            while i < nS:
                if S[i] != '#':
                    stack_S.append(S[i])
                else:
                    if len(stack_S) > 0:
                        out = stack_S.pop()
                i += 1
        
        if j < nT:
            while j < nT:
                if T[j] != '#':
                    stack_T.append(T[j])
                else:
                    if len(stack_T) > 0:
                        out = stack_T.pop()
                j += 1
        
        return stack_S == stack_T
		
# shorter stack solution
class Solution(object):
    def buildString(self, s):
        n = len(s)
        ans = []
        i = 0
        while i < n:
            if s[i] != '#':
                ans.append(s[i])
            else:
                if len(ans) > 0:
                    out = ans.pop()
            i += 1
            
        return ''.join(ans) 
        
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.buildString(S) == self.buildString(T)
        
# two pointers solution
