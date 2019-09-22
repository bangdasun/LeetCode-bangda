class Solution:
    def searchInRow(self, row, target):
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
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None:
            return False
        
        nrow = len(matrix)
        if nrow == 0:
            return False
        
        ncol = len(matrix[0])
        for row in range(nrow):
            if len(matrix[row]) > 0 and matrix[row][0] <= target <= matrix[row][-1]:
                search_result = self.searchInRow(matrix[row], target)
                if search_result:
                    return True
                
        return False
