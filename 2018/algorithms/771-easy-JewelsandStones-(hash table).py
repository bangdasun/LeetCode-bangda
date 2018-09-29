class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dct = {}
        for s in S:
            if s in dct.keys():
                dct[s] += 1
            else:
                dct[s] = 1
        
        cnt = 0
        for s in J:
            if s in dct.keys():
                cnt += dct[s]
                
        return cnt

# use same time		
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt = 0
        for s in J:
            cnt += S.count(s)
        
        return cnt