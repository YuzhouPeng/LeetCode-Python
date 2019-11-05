class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        length = len(S)
        count0 = S.count('0')
        count1 = 0
        res = length - count0
        for i in range(length):
            if S[i] == '0':
                count0 -= 1
            elif S[i] == '1':
                res = min(res, count0 + count1)
                count1 += 1
        return res