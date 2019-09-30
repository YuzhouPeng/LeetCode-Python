class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxvalue = max(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i] == maxvalue:
                index = i
        for i in range(len(nums)):
            if i != index and nums[i] * 2 > maxvalue:
                return -1

        return index