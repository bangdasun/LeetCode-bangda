class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {'(': ')', '[': ']', '{': '}'}
        output = True
        stack = []
        
        for i in s:
            if i in dct.keys():
                stack.append(i)
            if i in dct.values():
                # careful when stack is empty
                if len(stack) > 0:
                    left = stack.pop()
                else:
                    output = False
                    break
                if dct[left] != i:
                    output = False
                    break
                    
        n = len(stack)
        return output and n == 0