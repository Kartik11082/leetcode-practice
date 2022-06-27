class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        l = len(grid)
        for i in range(l):
            for j in range(l):
                if (i == j or i + j == (l - 1)):
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True