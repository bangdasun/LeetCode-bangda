class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        neg = num < 0
        num = abs(num)
        output = ''
        while num >= 0:
            output += str(num % 7)
            num = num // 7
            if num == 0:
                break
        
        return neg * '-' + output[::-1]