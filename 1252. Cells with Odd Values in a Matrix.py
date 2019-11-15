class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        count = 0
        array = [[0 for i in range(m)] for j in range(n)]
        # print(array)
        for indice in indices:
            for i in range(m):
                array[indice[0]][i] += 1
            for i in range(n):
                array[i][indice[1]] += 1
        for i in range(n):
            for j in range(m):
                if array[i][j] % 2 == 1:
                    count += 1
        return count
