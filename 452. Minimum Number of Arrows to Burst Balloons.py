class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        points.sort(key=lambda x:x[1])
        end = points[0][1]
        ans = 1
        for i in range(1,len(points)):
            if points[i][0] <= end:
                continue
            ans += 1
            end = points[i][1]

        return ans