class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.totalvalue = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def iteration(v, l):
            result = 0
            for dire in directions:
                if grid[v + dire[0]][l + dire[1]] == 1:
                    iteration(v + dire[0], l + dire[1])
                else:
                    self.totalvalue += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    iteration(i, j)
                    break
        return self.totalvalue

if __name__ == '__main__':
    sol = Solution
    sol.islandPerimeter(sol,[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])