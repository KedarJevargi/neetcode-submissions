class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count=0
        moves=[(-1,0),(0,1),(1,0),(0,-1)]
        row=len(grid)
        col=len(grid[0])

        def dfs(i,j):
            for move in moves:
                ni,nj=move
                if 0<=i+ni<row and 0<=j+nj<col and grid[ni+i][nj+j]=="1":
                    grid[ni+i][nj+j]="0"
                    dfs(ni+i,nj+j)


        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    islands_count+=1
                    dfs(i,j)

        return islands_count            

        