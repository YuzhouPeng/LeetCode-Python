class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        absnum = abs(x)
        basenum = 0
        flag = 0
        if x == 0:
            return 0
        while absnum != 0:
            i = absnum%10
            if i != 0:
                flag = 1
            if flag == 1:
                basenum = basenum*10+i
            absnum = absnum/10
        if (x<0 and basenum <= 2147483648):
            basenum = 0-basenum
            return basenum
        else:
            if basenum <= 2147483647:
                basenum = basenum
                return basenum
        return 0


