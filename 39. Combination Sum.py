def backtracking(tempcombination,combinations,start,target,candidate):
    if target==0:
        combinations.append(list(tempcombination))
        return
    for i in range(start,len(candidate)):
        if candidate[i]<=target:
            tempcombination.append(candidate[i])
            backtracking(tempcombination,combinations,i,target-candidate[i],candidate)
            tempcombination.remove(candidate[i])
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        backtracking([],combinations,0,target,candidates)
        return combinations