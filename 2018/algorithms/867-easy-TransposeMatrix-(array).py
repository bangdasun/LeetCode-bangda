class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        A_T = [[None] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                A_T[j][i] = A[i][j]
        
        return A_T