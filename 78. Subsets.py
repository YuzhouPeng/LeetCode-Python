def backtracking(size, tempsubset, subset, start,nums):
    if len(tempsubset)==size:
        subset.append(list(tempsubset))
        return
    for i in range(start,len(nums)):
        tempsubset.append(nums[i])
        backtracking(size,tempsubset,subset,i+1,nums)
        tempsubset.remove(nums[i])


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tempsubset = []
        subsetlist = []
        for i in range(len(nums)+1):
            backtracking(i,tempsubset,subsetlist,0,nums)
        return subsetlist