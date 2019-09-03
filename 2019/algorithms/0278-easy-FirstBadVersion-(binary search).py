# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            m = (left + right) // 2
            if isBadVersion(m):
                right = m - 1
            else:
                left = m + 1
        return left
