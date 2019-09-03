
from collections import deque

class Solution:
    def is_valid(self, grid, x, y):
        nrow = len(grid)
        ncol = len(grid[0])
        return 0 <= x < nrow and 0 <= y < ncol and grid[x][y] == 0
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid is None:
            return grid
        
        nrow = len(grid)
        if nrow == 0:
            return grid
        
        ncol = len(grid[0])
        if grid[0][0] == 1:
            return -1
        
        distance = 1
        queue = deque([(0, 0)])
        visited = set((0, 0))
        transform_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                            (0, 1), (1, -1), (1, 0), (1, 1)]
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in transform_coords:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if not self.is_valid(grid, next_x, next_y):
                        continue
                    if (next_x, next_y) in visited:
                        continue
                    if next_x + 1 == nrow and next_y + 1 == ncol:
                        return distance + 1
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
            distance += 1
            
        return -1
 