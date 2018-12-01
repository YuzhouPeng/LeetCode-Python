class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            maxvalue = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    maxvalue = max(dp[j]+1,maxvalue)

            dp[i]=maxvalue
        ret = 0
        for i in range(n):
            ret = max(ret,dp[i])
        return ret