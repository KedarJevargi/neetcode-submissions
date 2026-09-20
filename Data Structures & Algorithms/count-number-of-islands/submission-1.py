class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves=[(-1,0),(0,1),(1,0),(0,-1)]
        row=len(grid)
        col=len(grid[0]) 
        count=0

        visited=[[0]*col for i in range(row)]

        def dfs(i,j):
            for move in moves:
                ni,nj=move
                ni+=i
                nj+=j
                if 0<=ni<row and 0<=nj<col and grid[ni][nj]=="1" and visited[ni][nj]==0:
                    visited[ni][nj]=1
                    dfs(ni,nj)

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and visited[i][j]==0:
                    count+=1
                    visited[i][j]=1
                    dfs(i,j)
        return count            


        