class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = list()
        b= list()
        absnum = abs(x)
        lennum = 0
        i=0
        if (x == 0):
            return True
        if (x < 0):
            return False
        while absnum != 0:
            lennum = lennum + 1
            a.append(absnum%10)
            absnum = absnum / 10
        while i<lennum:
            k = a[lennum-(i+1)]
            b.append(k)
            i = i+1
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True