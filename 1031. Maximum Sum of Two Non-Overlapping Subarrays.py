class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1,len(A)):
            A[i]+=A[i-1]
        res, lmax,mmax = A[L+M-1],A[L-1],A[M-1]
        for i in range(L+M,len(A)):
            lmax = max(lmax,A[i-M]-A[i-L-M])
            mmax = max(mmax,A[i-L]-A[i-L-M])
            res = max(res,lmax+A[i]-A[i-M],mmax+A[i]-A[i-L])
        return res