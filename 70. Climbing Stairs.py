class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        pre2 = 1
        pre1 = 2
        for i in range(2,n):
            cur = pre2+pre1
            pre2=pre1
            pre1=cur
        return pre1