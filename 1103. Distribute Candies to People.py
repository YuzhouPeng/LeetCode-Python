class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        i = 1
        while candies > 0:
            res[(i % num_people) - 1] += min(candies, i)
            candies -= i
            i += 1
        return res
