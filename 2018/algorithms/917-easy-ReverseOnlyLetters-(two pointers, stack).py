# two pointers solution
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, j = 0, len(S) - 1
        str_list = list(S)
        letters =  'abcdefghijklmnopqrstuvwxyz'
        letters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while i < j:
            if S[i] not in letters:
                i += 1
                continue
            if S[j] not in letters:
                j -= 1
                continue
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        
        return ''.join(str_list)

# stack solution
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [c for c in S if c.isalpha()]
        ans = []
        for s in S:
            if s.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(s)
        
        return ''.join(ans)