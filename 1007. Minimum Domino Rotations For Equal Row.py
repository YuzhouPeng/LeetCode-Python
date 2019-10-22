class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        for x in range(1, 7):
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1