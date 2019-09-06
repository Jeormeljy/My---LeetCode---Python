'''

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:

11110
11010
11000
00000

Output: 1

Example 2:

Input:

11000
11000
00100
00011

Output: 3

'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = []
        for index in range(rows):
            visited.append([False] * cols)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.DFS(grid, rows, cols, visited, i, j)
                    count += 1
        return count
    
    def DFS(self, grid, rows, cols, visited, x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols or visited[x][y] or grid[x][y] != '1':
            return
        visited[x][y] = True
        self.DFS(grid, rows, cols, visited, x + 1, y)
        self.DFS(grid, rows, cols, visited, x - 1, y)
        self.DFS(grid, rows, cols, visited, x, y + 1)
        self.DFS(grid, rows, cols, visited, x, y - 1)
        
