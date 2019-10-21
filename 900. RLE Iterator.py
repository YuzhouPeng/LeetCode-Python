class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.q = collections.deque([])
        for i in range(0, len(A), 2):
            if A[i] > 0:
                self.q.append((A[i], A[i + 1]))

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n > 0 and self.q:
            count, number = self.q.popleft()
            if count >= n:
                count -= n
                if count > 0:
                    self.q.appendleft((count, number))
                return number
            else:
                n -= count
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)