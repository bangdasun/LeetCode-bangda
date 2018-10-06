class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
        dct = {}
        for i in range(26):
            dct[LETTERS[i]] = letters[i]
            
        str_list = list(str)
        for idx, s in enumerate(str_list):
            if s in dct.keys():
                str_list[idx] = dct[s]
                
        return ''.join(str_list)