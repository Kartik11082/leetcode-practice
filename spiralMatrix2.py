class Solution:
    def generateMatrix(self, n):
        left, right, top, bottom = 0, n-1 , 0, n-1
        res = [[0 for i in range(n)] for j in range(n)]
        val = 1
        while (val <= n*n):
            for i in range(left, right + 1):
                res[top][i] = val
                val += 1
            top += 1
            for i in range(top, bottom + 1):
                res[i][right] = val
                val += 1
            right -= 1
            for i in reversed(range(left, right + 1)):
                res[bottom][i] = val
                val += 1
            bottom -= 1
            for i in reversed(range(top, bottom + 1)):
                res[i][left] = val
                val += 1
            left += 1
        return res
