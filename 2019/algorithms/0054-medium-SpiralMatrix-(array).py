class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        nrow = len(matrix)
        if nrow == 0:
            return output
        
        ncol = len(matrix[0])
        
        row_low, row_up = 0, nrow - 1
        col_low, col_up = 0, ncol - 1
        
        row, col = 0, 0
        while len(output) < nrow * ncol:
            
            for col in range(col_low, col_up + 1):
                output.append(matrix[row][col])
            row_low += 1
            if len(output) == nrow * ncol:
                break
            
            for row in range(row_low, row_up + 1):
                output.append(matrix[row][col])
            col_up -= 1
            if len(output) == nrow * ncol:
                break
            
            for col in range(col_up, col_low - 1, -1):
                output.append(matrix[row][col])
            row_up -= 1
            if len(output) == nrow * ncol:
                break
            
            for row in range(row_up, row_low - 1, -1):
                output.append(matrix[row][col])
            col_low += 1
            if len(output) == nrow * ncol:
                break
            
        return output
