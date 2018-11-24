def backtracking(combinlist,combinations,visited,start,target,candidates):
    if target==0:
        combinations.append(list(combinlist))
        return
    for i in range(start,len(candidates)):
        if i!=0 and candidates[i]==candidates[i-1] and visited[i-1]==0:
            continue
        if candidates[i]<=target:
            combinlist.append(candidates[i])
            visited[i]=1
            backtracking(combinlist,combinations,visited,i+1,target-candidates[i],candidates)
            visited[i]=0
            combinlist.remove(candidates[i])


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        candidates.sort()
        visited = [0]*len(candidates)
        backtracking([],combinations,visited,0,target,candidates)
        return combinations

if __name__ == '__main__':
    sol= Solution
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(sol.combinationSum2(sol,candidates,target))