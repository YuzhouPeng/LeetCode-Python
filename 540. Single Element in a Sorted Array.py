class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length1 = len(nums)
        l = 0
        r = length1-1
        while l<r:
            m = l+(r-l)/2
            if m%2==1:
                m -=1
            if nums[m]==nums[m+1]:
                l = m+2
            else:
                r = m
        return nums[l]