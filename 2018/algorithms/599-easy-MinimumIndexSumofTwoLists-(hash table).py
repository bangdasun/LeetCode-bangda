class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        n1, n2 = len(list1), len(list2)
        
        dct = {}
        curr_min = n1 + n2
        output = []
        if n1 < n2:
            for idx, r in enumerate(list1):
                dct[r] = idx
            
            for idx, r in enumerate(list2):
                if r in dct.keys():
                    idx_sum = idx + dct[r]
                    if curr_min >= idx_sum:
                        curr_min = idx_sum
                        output.append(r)
        else:
            for idx, r in enumerate(list2):
                dct[r] = idx
                
            for idx, r in enumerate(list1):
                if r in dct.keys():
                    idx_sum = idx + dct[r]
                    if curr_min >= idx_sum:
                        curr_min = idx_sum
                        output.append(r)
        
        return output