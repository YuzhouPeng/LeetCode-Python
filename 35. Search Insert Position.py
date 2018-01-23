class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numslen = len(nums)
        if numslen == 0:
            return 0
        for i in range(numslen):
            if nums[i] == target:
                return i
        for i in range(numslen):
            if target <= nums[i]:
                return i
        return numslen