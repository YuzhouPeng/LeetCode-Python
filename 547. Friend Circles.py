def dfs(M,curr,n):
    for i in range(n):
        if M[curr][i]==1:
            M[curr][i] = M[i][curr]=0
            dfs(M,i,n)


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circleNum = 0
        for i in range(n):
            if M[i][i]==1:
                circleNum+=1
                dfs(M,i,n)
        return circleNum