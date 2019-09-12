class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        newstr = str(bin(int(n)))
        for s in newstr:
            if s=="1":
                count+=1
        return count