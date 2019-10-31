import collections
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        return sum(v * (v - 1) / 2 for v in collections.Counter(tuple(sorted(x)) for x in dominoes).values())