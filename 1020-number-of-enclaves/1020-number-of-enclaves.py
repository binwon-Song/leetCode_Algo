class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            dx=[0,0,1,-1]
            dy=[1,-1,0,0]
            for idx in range(4):
                nx=j+dx[idx]
                ny=i+dy[idx]
                if 0 <= ny < m and 0 <= nx < n and grid[ny][nx]:
                    dfs(ny, nx)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)