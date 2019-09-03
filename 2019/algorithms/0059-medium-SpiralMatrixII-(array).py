class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        row_low, row_up = 0, n - 1
        col_low, col_up = 0, n - 1
        
        i = 1
        row, col = 0, 0
        while i <= n ** 2:
            
            if i > n ** 2:
                break
            for col in range(col_low, col_up + 1):
                matrix[row][col] = i
                i += 1
            row_low += 1
            
            if i > n ** 2:
                break
            for row in range(row_low, row_up + 1):
                matrix[row][col] = i
                i += 1
            col_up -= 1
            
            if i > n ** 2:
                break
            for col in range(col_up, col_low - 1, -1):
                matrix[row][col] = i
                i += 1
            row_up -= 1
            
            if i > n ** 2:
                break
            for row in range(row_up, row_low - 1, -1):
                matrix[row][col] = i
                i += 1
            col_low += 1
            
        return matrix
