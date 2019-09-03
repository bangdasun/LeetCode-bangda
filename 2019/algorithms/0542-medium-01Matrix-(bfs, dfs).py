
from collections import deque

class Solution:
    def is_valid(self, matrix: List[List[int]], x: int, y: int):
        nrow = len(matrix)
        if nrow == 0:
            return False
        
        ncol = len(matrix[0])
        return 0 <= x < nrow and 0 <= y < ncol
    
    def bfs(self, matrix: List[List[int]], x: int, y: int, distance: List[List[int]]) -> List[List[int]]:
        queue = deque([(x, y)])
        visited = set((x, y))
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for delta_i, delta_j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    next_i = i + delta_i
                    next_j = j + delta_j
                    if not self.is_valid(matrix, next_i, next_j):
                        continue
                    if (next_i, next_j) in visited:
                        continue
                    if matrix[next_i][next_j] == 0:
                        return distance
                    queue.append((next_i, next_j))
                    visited.add((next_i, next_j))
            distance[x][y] += 1
        return distance
                    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix is None:
            return matrix
        
        nrow = len(matrix)
        if nrow == 0:
            return matrix
        
        ncol = len(matrix[0])
        distance = [[0 for j in range(ncol)] for i in range(nrow)]
        
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 1:
                    distance[i][j] += 1
                    distance = self.bfs(matrix, i, j, distance)
        
        return distance
