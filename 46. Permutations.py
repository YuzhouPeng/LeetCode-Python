class Solution:
    def dfs(self, Nums, sublist):
        if len(sublist) == len(Nums):
            self.res.append(sublist[:])
        for m in Nums:
            if m in sublist:
                continue
            sublist.append(m)
            self.dfs(Nums, sublist)
            sublist.remove(m)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(nums,sub)
        return self.res

