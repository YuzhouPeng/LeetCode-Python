class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        prefix = 0
        count = [1]+[0]*(K)
        for a in A:
            prefix = (prefix+a)%k
            res+=count[prefix]
            count[prefix]+=1
        return res