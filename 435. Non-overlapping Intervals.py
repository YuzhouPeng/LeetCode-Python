# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals)==0:
            return 0
        invs = sorted((x.end,x.start) for x in intervals)
        end = -0x7FFFFFFF
        ans = 0
        for e,s in invs:
            if s >=end:
                end = e
                ans += 1
        return len(intervals) -ans