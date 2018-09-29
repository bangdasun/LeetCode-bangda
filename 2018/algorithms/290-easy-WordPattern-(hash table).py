class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        len_p = len(pattern)
        str_list = str.split(' ')
        len_s = len(str_list)
        if len_p != len_s:
            return False
        
        bijection = {}
        for idx, p in enumerate(pattern):
            if p in bijection.keys():
                if bijection[p] != str_list[idx]:
                    return False
            else:
                # notice do not add key - value directly, also need to check if value is in the hash table
                if str_list[idx] not in bijection.values():
                    bijection[p] = str_list[idx]
                else:
                    return False
                
        return True