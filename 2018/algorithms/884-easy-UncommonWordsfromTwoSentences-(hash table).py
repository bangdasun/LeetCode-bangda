# my AC
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dct_A = {}
        dct_B = {}
        w_list_A = A.split(' ')
        w_list_B = B.split(' ')
        uncommon_list = []
        
        for w in w_list_A:
            dct_A[w] = dct_A.get(w, 0) + 1
        
        for w in w_list_B:
            dct_B[w] = dct_B.get(w, 0) + 1
        
        for w, cnt in dct_A.items():
            if cnt == 1 and w not in dct_B.keys():
                uncommon_list.append(w)
        
        for w, cnt in dct_B.items():
            if cnt == 1 and w not in dct_A.keys():
                uncommon_list.append(w)
                
        return uncommon_list
        
# less space consumption
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dct = {}
        w_list_A = A.split(' ')
        w_list_B = B.split(' ')
        uncommon_list = []
        
        for w in w_list_A:
            dct[w] = dct.get(w, 0) + 1
        
        for w in w_list_B:
            dct[w] = dct.get(w, 0) + 1
        
        for w, cnt in dct.items():
            if cnt == 1:
                uncommon_list.append(w)
       
        return uncommon_list