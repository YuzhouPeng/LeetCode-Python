class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        suma = sum(A)
        sumb = sum(B)
        setB = set(B)
        for a in A:
            if a+(sumb-suma)/2 in setB:
                return [a,a+(sumb-suma)/2]