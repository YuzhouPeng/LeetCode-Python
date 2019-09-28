class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        minpair = []
        minv = float("inf")
        for i in range(1,len(arr)):
            minvalue = arr[i]-arr[i-1]
            if minv>minvalue:
                minpair = [[arr[i-1],arr[i]]]
                minv = minvalue
            elif minv==minvalue:
                minpair.append([arr[i-1],arr[i]])
        return minpair