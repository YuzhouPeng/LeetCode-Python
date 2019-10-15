import collections
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp, m, n = collections.defaultdict(int),len(A),len(B)
        for i in range(m):
            for j in range(n):
                dp[i,j] = max(dp[i-1,j-1]+(A[i]==B[j]),dp[i-1,j],dp[i,j-1])
        return dp[m-1,n-1]


if __name__ == '__main__':
    sol = Solution()
    sol.maxUncrossedLines([1,4,2]
,[1,2,4])