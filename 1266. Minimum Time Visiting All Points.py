class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for prev, current in zip(points, points[1:]):
            maxvalue = -1
            for p, c in zip(prev, current):
                maxvalue = max(maxvalue, abs(p - c))
            res += maxvalue
        return res

