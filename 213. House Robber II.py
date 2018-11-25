def robdp(nums, first, last):
    pre2 = 0
    pre1 = 0
    for i in range(first,last+1):
        cur = max(pre1,pre2+nums[i])
        pre2 = pre1
        pre1 = cur
    return pre1

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        n = len(nums)
        if n==1:
            return nums[0]
        return max(robdp(nums,0,n-2),robdp(nums,1,n-1))