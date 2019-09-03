"""
	Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
	Return -1 if destination cannot be reached.

	If the knight is at (x, y), he can get to the following positions in one step:

	(x + 1, y + 2)
	(x + 1, y - 2)
	(x - 1, y + 2)
	(x - 1, y - 2)
	(x + 2, y + 1)
	(x + 2, y - 1)
	(x - 2, y + 1)
	(x - 2, y - 1)
	
	source and destination must be empty.
	Knight can not enter the barrier.
	Path length refers to the number of steps the knight takes.

"""


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def is_reachable(self, grid, point, visited):
        nrow = len(grid)
        ncol = len(grid[0])
        x, y = point.x, point.y
        return 0 <= x < nrow and 0 <= y < ncol and (x, y) not in visited and grid[x][y] == 0
    
    def shortestPath(self, grid, source, destination):
        queue = deque([source])
        visited = set((source.x, source.y))
        n_steps = 0
        transform_coord = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                           (2, 1), (2, -1), (-2, 1), (-2, -1)]
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                point = queue.popleft()
                for delta_x, delta_y in transform_coord:
                    next_x = point.x + delta_x
                    next_y = point.y + delta_y
                    new_point = Point(a=next_x, b=next_y)
                    
                    if not self.is_reachable(grid, new_point, visited):
                        continue
                    
                    if new_point.x == destination.x and new_point.y == destination.y:
                        return n_steps + 1
                    
                    queue.append(new_point)
                    visited.add((new_point.x, new_point.y))
            n_steps += 1
        
        return -1
