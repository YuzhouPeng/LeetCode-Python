class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2 or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        des = list(nums[::-1])
        aes = list(nums)
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1, len(nums)):
            aes[i] = aes[i - 1] + aes[i]
        # print(aes)
        for i in range(1, len(nums)):
            des[i] = des[i - 1] + des[i]
        des = list(des[::-1])
        # print(des)

        for i in range(1, len(nums) - 1):
            if aes[i - 1] == des[i + 1]:
                return i
        # print(sum(nums[1:]))

        if sum(nums[:len(nums) - 1]) == 0:
            return len(nums) - 1
        # print(sum(nums[:len(nums)-1]))
        return -1
