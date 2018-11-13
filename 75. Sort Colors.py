def swap(nums, i,j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1
        one = 0
        two = len(nums)
        while one<two:
            if nums[one]==0:
                swap(nums,zero+1,one)
                zero = zero+1
                one = one+1
            elif nums[one]==2:
                swap(nums, one,two-1)
                two = two-1
            else:
                one = one+1

