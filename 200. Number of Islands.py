direction = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(grid,c,r,m,n):
    if c<0 or c>=m or r<0 or r>=n or grid[c][r]=='0':
        return
    grid[c][r] = '0'
    for d in direction:
        dfs(grid,c+d[0],r+d[1],m,n)
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid==None or len(grid)==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        islandsum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!='0':
                    dfs(grid,i,j,m,n)
                    islandsum+=1
        return islandsum