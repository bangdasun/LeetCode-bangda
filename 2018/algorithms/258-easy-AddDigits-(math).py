class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = 0
        while num % 10 != num:
            while num > 0:
                s += num % 10
                num = num // 10
                
            # sum operation ends - update num and reset s
            if num == 0:
                num = s
                s = 0
            
        return num

# Smart solution
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
		
		# a * (10 ** n) % 9 == a % 9
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9