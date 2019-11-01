class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        result = []
        count = 0
        for i in arr:
            if i != 0:
                result.append(i)
            else:
                result.append(0)
                result.append(0)
        for i in range(len(arr)):
            arr[i] = result[i]
