# brute force solution
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        A_list = list(A)
        B_list = list(B)
        if len(A) != len(B):
            return False
        
        if A == B:
            return True
        
        n = len(A)
        for i in range(n):
            if A_list != B_list:
                A_list.append(A_list.pop(0))
            else:
                return True
        
        return False

# simple check solution
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A + A
		
