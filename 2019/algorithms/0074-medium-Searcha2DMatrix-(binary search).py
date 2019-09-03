class Solution:
    def searchInRow(self, row: List[int], target: int) -> bool:
        if row is None:
            return False
        
        n = len(row)
        if n == 0:
            return False
        
        if n == 1:
            return row[0] == target
        
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if row[mid] < target:
                start = mid
            elif row[mid] == target:
                return True
            else:
                end = mid
        
        return row[start] == target or row[end] == target
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False
        
        nrow = len(matrix)
        if nrow == 0:
            return False
        
        for i in range(nrow):
            if len(matrix[i]) > 0 and matrix[i][0] <= target <= matrix[i][-1]:
                search_result = self.searchInRow(matrix[i], target)
                if search_result:
                    return True
        
        return False
