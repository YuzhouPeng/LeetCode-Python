def backtracking(start,size,tempsubset,subset,visited,nums):
    if len(tempsubset)==size:
        subset.append(list(tempsubset))
        return
    for i in range(start,len(nums)):
        if visited[i-1]==0 and i!=0 and nums[i]==nums[i-1]:
            continue
        tempsubset.append(nums[i])
        visited[i]=1
        backtracking(i+1,size,tempsubset,subset,visited,nums)
        visited[i]=0
        tempsubset.remove(nums[i])

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subset = []
        paths = []
        visited = [0]*len(nums)
        for i in range(len(nums)+1):
            backtracking(0,i,paths,subset,visited,nums)
        return subset

if __name__ == '__main__':
    sol = Solution
    nums = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(sol.subsetsWithDup(sol,nums))