class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        numstr = str(n)
        productvalue = 1
        sumvalue = 0
        for i in numstr:
            productvalue *=int(i)
            sumvalue +=int(i)
        return productvalue-sumvalue