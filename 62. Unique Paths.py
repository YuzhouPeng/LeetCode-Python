class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j]+dp[j-1]
        return dp[n-1]

if __name__ == '__main__':
    sol = Solution
    print(sol.uniquePaths(sol,3,2))