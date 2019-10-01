class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        elements = {}
        for i, v in enumerate(nums):
            if v in elements and i-elements[v]<=k:
                return True
            elements[v] = i
        return False