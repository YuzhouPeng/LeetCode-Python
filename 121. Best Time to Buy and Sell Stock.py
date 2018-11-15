class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pricelens = len(prices)
        if pricelens==0:
            return 0
        minsum = prices[0]
        maxvalue = 0
        for i in range(1,pricelens):
            if minsum>prices[i]:
                minsum=prices[i]
            else:
                maxvalue = max(maxvalue,prices[i]-minsum)
        return maxvalue
