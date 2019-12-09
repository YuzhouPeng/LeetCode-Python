class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        res = 0
        j = 0
        for i in range(len(A)):
            if A[i]>=L and A[i]<=R:
                res+=i-j+1
                count=i-j+1
            elif A[i]<L:
                res+=count
            else:
                j = i+1
                count=0
        return res