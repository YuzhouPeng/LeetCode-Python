
class Solution:

    def dfs(self, Nums, sublist,flaglist):
        if len(sublist) == len(Nums) and sublist not in self.res:
            self.res.append(sublist[:])
        last = None
        for indexp in range(len(Nums)):
            m = Nums[indexp]
            if flaglist[indexp]==1:
                continue
            if last==m:
                continue
            flaglist[indexp]=1
            sublist.append(m)
            self.dfs(Nums,sublist,flaglist)
            last = sublist.pop()
            flaglist[indexp]=0
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        flaglist = [0]*len(nums)
        nums = sorted(nums)
        self.dfs(nums,sub,flaglist)
        return self.res
