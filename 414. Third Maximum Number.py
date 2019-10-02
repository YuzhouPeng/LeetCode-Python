import collections
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        length = len(counter.keys())
        if length < 3:
            return max(counter.keys())
        i = 0
        elements = list(counter.keys())
        # print(elements)
        while i < 2:
            maxvalue = max(elements)
            for index, k in enumerate(elements):
                if k == maxvalue:
                    elements.pop(index)
                    # print(elements)
            i += 1

        return max(elements)