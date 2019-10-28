import collections
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        res = 0
        for t in time:
            res+=counter[(-t%60)]
            counter[t%60]+=1
        return res