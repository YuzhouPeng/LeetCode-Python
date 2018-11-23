def backtracking(combinlist, combinations,start,k,n):
    if k==0:
        combinations.append(list(combinlist))
        return
    for i in range(start,n-k+2):
        combinlist.append(i)
        backtracking(combinlist,combinations,i+1,k-1,n)
        combinlist.remove(i)
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        combinlist = []
        backtracking(combinlist,combinations,1,k,n)
        return combinations
