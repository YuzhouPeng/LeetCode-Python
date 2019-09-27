class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        result = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
                result = max(result,count)
            else:
                count = 1
        return result