
from collections import deque

class Solution:
    def not_rotten(self, grid, x, y):
        nrow = len(grid)
        ncol = len(grid[0])
        return 0 <= x < nrow and 0 <= y < ncol and grid[x][y] == 1
    
    def get_start(self, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        output = []
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    output.append((i, j))
        return output
    
    def exist_fresh(self, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        output = []
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    return True
        return False
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return -1
        
        nrow = len(grid)
        if nrow == 0:
            return -1
        
        ncol = len(grid[0])
        starts = self.get_start(grid)
        if len(starts) == 0:
            if self.exist_fresh(grid):
                return -1
            else:
                return 0
        
        queue = deque(starts)
        minute = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if not self.not_rotten(grid, next_x, next_y):
                        continue
                    grid[next_x][next_y] = 2
                    queue.append((next_x, next_y))
            if len(queue) > 0:
                minute += 1
        
        if self.exist_fresh(grid):
            return -1
        
        return minute
