def binarysearch(nums,target):
    l=0
    r = len(nums)
    while l<r:
        m = l+(r-l)/2
        if nums[m]>=target:
            r = m
        else:
            l = m+1
    return l

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        coordlist = []
        l=0
        length1 = len(nums)
        first = binarysearch(nums,target)
        last = binarysearch(nums,target+1)-1
        if first == length1 or nums[first]!= target:
            return [-1,-1]
        else:
            return [first,max(first,last)]
