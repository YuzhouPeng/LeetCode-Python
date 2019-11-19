class Solution(object):
    def shiftGrid(self, grid, k):
        f1 = lambda col, nums: [nums[i:i+col] for i in range(0, len(nums), col)]
        f2 = lambda nums, k: nums[-k%len(nums):] + nums[:-k%len(nums)]
        return f1(len(grid[0]), f2(sum(grid, []), k))