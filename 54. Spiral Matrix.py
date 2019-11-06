class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        if len(matrix) == 0:
            return []
        rowbegin = 0
        rowend = len(matrix) - 1
        colbegin = 0
        colend = len(matrix[0]) - 1
        while (rowbegin <= rowend and colbegin <= colend):
            for i in range(colbegin, colend + 1):
                res.append(matrix[rowbegin][i])
            rowbegin += 1
            for i in range(rowbegin, rowend + 1):
                res.append(matrix[i][colend])
            colend -= 1
            if rowbegin <= rowend:
                for i in range(colend, colbegin - 1, -1):
                    res.append(matrix[rowend][i])
            rowend -= 1
            if colbegin <= colend:
                for i in range(rowend, rowbegin - 1, -1):
                    res.append(matrix[i][colbegin])
            colbegin += 1
        return res


