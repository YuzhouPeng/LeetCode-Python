class Solution(object):
    def countServers(self, A):
        X,Y = map(sum,A),map(sum,zip(*A))
        return sum(X[i]+Y[j]>2 for i in range(len(A)) for j in range(len(A[0])) if A[i][j])