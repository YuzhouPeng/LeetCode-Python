class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length1 = len(nums)
        l=0
        r = length1-1
        while l<r:
            m = l+(r-l)/2
            if nums[m]<=nums[l]:
                r = m
            else:
                l = m+1
        return nums[l]
