class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        if n==0:
            return []
        rowbegin = 0
        rowend = len(matrix)-1
        colbegin = 0
        colend = len(matrix[0])-1
        count = 1
        while (rowbegin<=rowend and colbegin<=colend):
            for i in range(colbegin,colend+1):
                matrix[rowbegin][i] = count
                count+=1
            rowbegin+=1
            for i in range(rowbegin,rowend+1):
                matrix[i][colend] = count
                count+=1
            colend-=1
            if rowbegin<=rowend:
                for i in range(colend,colbegin-1,-1):
                    matrix[rowend][i] = count
                    count+=1
            rowend-=1
            if colbegin <=colend:
                for i in range(rowend,rowbegin-1,-1):
                    matrix[i][colbegin] = count
                    count+=1
            colbegin+=1
        return matrix