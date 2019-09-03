class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        if m < 2 or n < 2:
            return 1
        
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][1] = 1
        matrix[1][0] = 1
        
        for i in range(m):
            matrix[i][0] = 1
            
        for j in range(n):
            matrix[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        
        return matrix[-1][-1]
