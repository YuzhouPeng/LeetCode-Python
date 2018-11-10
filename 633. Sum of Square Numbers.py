import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a =0
        b = int(math.sqrt(c))
        while a<b:
            sum = a*a+b*b
            if sum == c:
                return True
            elif sum>c:
                b = b-1
            else:
                a = a+1

        return False
