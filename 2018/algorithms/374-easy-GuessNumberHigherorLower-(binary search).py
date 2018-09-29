# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            m = (right + left) // 2
            # my guess is higher
            if guess(m) < 0:
                right = m - 1
            # my guess is lower
            elif guess(m) > 0:
                left = m + 1
            else:
                return m
        return -1