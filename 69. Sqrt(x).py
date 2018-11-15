class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        l = 1
        r = x
        while l<=r:
            mid = l+(r-l)/2
            sqrt = x/mid
            if sqrt==mid:
                return mid
            elif mid>sqrt:
                r = mid-1
            else:
                l = mid+1

        return r