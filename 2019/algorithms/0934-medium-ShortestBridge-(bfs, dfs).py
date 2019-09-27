
from collections import deque

class Solution:
    def is_inbounds_island(self, A, x, y, visited):
        nrow = len(A)
        ncol = len(A[0])
        return 0 <= x < nrow and 0 <= y < ncol and A[x][y] == 1 and (x, y) not in visited
    
    def bfs(self, A, x, y):
        queue = deque([(x, y)])
        visited = set([(x, y)])
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_i = i + delta_i
                    next_j = j + delta_j
                    if not self.is_inbounds_island(A, next_i, next_j, visited):
                        continue
                    queue.append((next_i, next_j))
                    visited.add((next_i, next_j))
        return visited
    
    def getStartIsland(self, A):
        nrow = len(A)
        ncol = len(A[0])
        for i in range(nrow):
            for j in range(ncol):
                if A[i][j] == 0:
                    continue
                visited = self.bfs(A, i, j)
                return list(visited)
        return []
    
    def shortestBridge(self, A: List[List[int]]) -> int:
        if A is None:
            return None
        
        nrow = len(A)
        if nrow == 0:
            return None
        
        ncol = len(A[0])
        starts = self.getStartIsland(A)
        
        queue = deque(starts)
        visited = set(starts)
        flip = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if (next_x, next_y) in visited:
                        continue
                    if next_x < 0 or next_x >= nrow or next_y < 0 or next_y >= ncol:
                        continue
                    if A[next_x][next_y] == 1:
                        return flip
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
            flip += 1
        
        return None
