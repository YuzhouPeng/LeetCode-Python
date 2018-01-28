class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = float('-inf')
        numsLen = len(nums)
        if numsLen == 0:
            return -1
        if numsLen == 1:
            return nums[0]
        for i in range(numsLen):
            for j in range(i+1, numsLen+1):
                for k in range(i,j):
                    sum = sum + nums[k]
                if max <= sum:
                    max = sum
                    sum = 0
                else:
                    sum = 0

        return max