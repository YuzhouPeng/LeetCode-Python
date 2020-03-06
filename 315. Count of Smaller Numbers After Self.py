class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum)/2
            if half:
                left,right = sort(enum[:half]),sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not left or right and left[-1][1]>right[-1][1]:
                        result[left[-1][0]]+=len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        result = [0]*len(nums)
        enums = sort(list(enumerate(nums)))
        return result


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]