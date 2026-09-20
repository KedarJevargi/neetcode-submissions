class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            area = 1

            for di, dj in moves:
                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    area += dfs(ni, nj)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area