class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        n = len(A)
        for left in range(n - 2, -1, -1):
            if A[left] > A[left + 1]:
                break
        else:
            return A
        print(left)
        right = A.index(max(a for a in A[left + 1:] if a < A[left]), left)
        print(right)
        A[left], A[right] = A[right], A[left]
        return A
