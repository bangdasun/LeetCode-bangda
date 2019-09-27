from collections import deque

# similar with:
# 542 01 Matrix
# 994 Rotting Oranges
class Solution:
    def is_unknown_water(self, grid: List[List[int]], x, y, visited) -> bool:
        nrow = len(grid)
        ncol = len(grid[0])
        return 0 <= x < nrow and 0 <= y < ncol and (x, y) not in visited and grid[x][y] == 0
    
    def get_islands(self, grid: List[List[int]]):
        if grid is None:
            return []
        
        nrow = len(grid)
        ncol = len(grid[0])
        output = []
        
        for x in range(nrow):
            for y in range(ncol):
                if grid[x][y] == 0:
                    continue
                output.append((x, y))
        return output
        
    def maxDistance(self, grid: List[List[int]]) -> int:
        if grid is None:
            return -1
        
        nrow = len(grid)
        if nrow == 0:
            return -1
        
        ncol = len(grid[0])
        sum_grid = sum([sum(grid[i]) for i in range(nrow)])
        if sum_grid == 0 or sum_grid == nrow * ncol:
            return -1
        
        max_distance = 0
        visited = set()
        all_islands = self.get_islands(grid)
        queue = deque(all_islands)
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if not self.is_unknown_water(grid, next_x, next_y, visited):
                        continue
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    
            if len(queue) > 0:
                max_distance += 1
        
        return max_distance
