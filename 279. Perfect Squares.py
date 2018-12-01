class Solution(object):
    def numSquares(self, n):
        dp = [0]+ [float("inf")] * n
        for i in range(1, int(n**0.5)+1):
            for j in range(i**2, n+1):
                dp[j] = min(dp[j], dp[j-i**2]+1)
        return dp[-1]