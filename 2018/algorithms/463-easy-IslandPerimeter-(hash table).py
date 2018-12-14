# refer from http://www.cnblogs.com/grandyang/p/6096138.html
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        
        col = len(grid[0])
        if col == 0:
            return 0
        
        p = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                if c == 0 or grid[r][c-1] == 0:
                    p += 1
                if  r == 0 or grid[r-1][c] == 0:
                    p += 1
                if c == col - 1 or grid[r][c+1] == 0:
                    p += 1
                if r == row - 1 or grid[r+1][c] == 0:
                    p += 1
        
        return p