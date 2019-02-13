direction = [[0,1],[0,-1],[1,0],[-1,0]]
# def dfs(grid,r,c,m,n):
#     if  r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
#         return 0
#     grid[r][c]=0
#     area=1
#     for d in direction:
#         area += dfs(grid, r+d[0],c+d[1],m,n)
#     return area
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(grid,r,c,m,n):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
                return 0
            area = 1
            for i in range(len(direction)):
                area+=dfs(grid,r+direction[i][0],c+direction[i][1],m,n)
            return area
        if grid==None or len(grid)==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea,dfs(grid,i,j,m,n))
        return maxArea