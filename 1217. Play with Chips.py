class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        even_parity = 0
        odd_parity = 0
        for chip in chips:
            if chip % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
        return min(even_parity, odd_parity)