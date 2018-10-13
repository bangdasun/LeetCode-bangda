class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ncol = len(A[0])
        for idx, row in enumerate(A):
            left, right = 0, ncol - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
            A[idx] = [0 if x == 1 else 1 for x in row]
            
        return A