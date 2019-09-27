
from collections import deque

class Solution:
    def on_boardO(self, board, x, y):
        nrow = len(board)
        ncol = len(board[0])
        if 0 < x < nrow - 1 and 0 < y < ncol - 1:
            return False
        return board[x][y] == 'O'
    
    def in_boundsO(self, board, x, y):
        nrow = len(board)
        ncol = len(board[0])
        return 0 <= x < nrow and \
               0 <= y < ncol and \
               board[x][y] == 'O'
    
    def get_onboardO(self, board):
        nrow = len(board)
        ncol = len(board[0])
        onboard = []
        for i in range(nrow):
            for j in range(ncol):
                if not self.on_boardO(board, i, j):
                    continue
                onboard.append((i, j))
        return onboard
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None:
            return None
        
        nrow = len(board)
        if nrow == 0:
            return None
        
        ncol = len(board[0])
        starts = self.get_onboardO(board)
        queue = deque(starts)
        visited = set(starts)
        while len(queue) > 0:
            i, j = queue.popleft()
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i = i + delta_i
                next_j = j + delta_j
                if not self.in_boundsO(board, next_i, next_j):
                    continue
                if (next_i, next_j) in visited:
                    continue
                queue.append((next_i, next_j))
                visited.add((next_i, next_j))
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'X':
                    continue
                if (i, j) in visited:
                    continue
                board[i][j] = 'X'
                
        return None
