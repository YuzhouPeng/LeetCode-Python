class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre1 = 0
        pre2 = 0
        for i in range(len(nums)):
            cur = max(pre2+nums[i],pre1)
            pre2=pre1
            pre1 = cur

        return  pre1