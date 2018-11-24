def backtracking(k,n,start,tempcombination,combinations):
    if k==0 and n==0:
        combinations.append(list(tempcombination))
        return
    if k==0 or n==0:
        return
    for i in range(start,10):
        tempcombination.append(i)
        backtracking(k-1,n-i,i+1,tempcombination,combinations)
        tempcombination.remove(i)

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combinations = []
        path = []
        backtracking(k,n,1,path,combinations)
        return combinations