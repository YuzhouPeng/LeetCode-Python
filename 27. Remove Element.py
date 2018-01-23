class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        resultNum = list()
        numsLen = len(nums)
        if numsLen == 0:
            return -1
        if val == None:
            return numsLen
        for i in range(numsLen):
            if nums[i] != val:
                resultNum.append(nums[i])
        resultLen = len(resultNum)
        for i in range(resultLen):
            nums[i] = resultNum[i]
        return resultLen