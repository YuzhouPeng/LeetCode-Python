class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(arr)
        while ans != arr:
            ans = arr[:]
            for i in range(1, len(arr) - 1):
                arr[i] += (ans[i - 1] > ans[i] < ans[i + 1]) - (ans[i - 1] < ans[i] > ans[i + 1])
        return arr if len(arr) < 3 else ans
