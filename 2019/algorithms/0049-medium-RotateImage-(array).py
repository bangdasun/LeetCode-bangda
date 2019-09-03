class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])
        if nrow == ncol == 1:
            return matrix
        
        matrix_1d = []
        for i in range(nrow - 1, -1, -1):
            for j in range(ncol - 1, -1, -1):
                matrix_1d.append(matrix[i][j])
        
        for j in range(ncol):
            for i in range(nrow - 1, -1, -1):
                matrix[i][j] = matrix_1d.pop(0)
