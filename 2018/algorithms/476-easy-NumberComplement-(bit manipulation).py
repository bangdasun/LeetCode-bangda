class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = []
        if num < 2:
            if num:
                return 0
            else:
                return 1
            
        while num >= 2:
            output.append(num % 2)
            num = num // 2
        
        output.append(num % 2)
        
        for idx, val in enumerate(output):
            if val:
                output[idx] = 0
            else:
                output[idx] = 1
        
        n = len(output)
        output_num = 0
        for i in range(n - 1, -1, -1):
            output_num += output[i] * (2 ** i)
        
        return output_num