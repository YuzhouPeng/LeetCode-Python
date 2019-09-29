class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k==1:
            return max(nums)
        maxvalue = 0
        for i in range(k):
            maxvalue+=nums[i]
        itervalue = maxvalue

        for i in range(1,len(nums)):
            if i+k-1<len(nums):
                itervalue-=nums[i-1]
                itervalue+=nums[i+k-1]
            maxvalue = max(maxvalue,itervalue)
        result = float(maxvalue)/float(k)
        return result