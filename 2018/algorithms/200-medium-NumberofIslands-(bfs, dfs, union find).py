# refer from http://www.cnblogs.com/grandyang/p/4402656.html
class Solution:
    def search_dfs(self, grid, visited, x, y):
        if x < 0 or x >= len(grid):
            return
        
        if y < 0 or y >= len(grid[0]):
            return
        
        if grid[x][y] != '1' or visited[x][y]:
            return
        
        visited[x][y] = True
        self.search_dfs(grid, visited, x + 1, y)
        self.search_dfs(grid, visited, x - 1, y)
        self.search_dfs(grid, visited, x, y + 1)
        self.search_dfs(grid, visited, x, y - 1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        num = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    self.search_dfs(grid, visited, r, c)
                    num += 1
        
        return num