class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            for j in range(n):
                if i==0:
                    dp[j] = dp[j-1]
                else:
                    dp[j] = min(dp[j-1],dp[j])
                dp[j] += grid[i][j]

        return dp[n-1]