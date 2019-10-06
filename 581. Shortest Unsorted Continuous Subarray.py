class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not res else res[-1] - res[0] + 1
