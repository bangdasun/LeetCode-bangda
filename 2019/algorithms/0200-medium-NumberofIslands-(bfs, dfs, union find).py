
from collections import deque

class Solution:
    def is_unknow_island(self, grid, x, y, visited):
        nrow = len(grid)
        ncol = len(grid[0])
        return 0 <= x < nrow and 0 <= y < ncol and (x, y) not in visited and grid[x][y] == '1'
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while len(queue) > 0:
            x, y = queue.popleft()
            for delta_x, delta_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_unknow_island(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        return visited
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        nrow = len(grid)
        if nrow == 0:
            return 0
        
        ncol = len(grid[0])
        visited = set()
        num_islands = 0
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited = self.bfs(grid, i, j, visited)
                    num_islands += 1
        
        return num_islands
