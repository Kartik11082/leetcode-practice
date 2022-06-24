class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        setZeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setZeroes.append([i, j])

        for r, c in setZeroes:
            for t in range(0, len(matrix[0])):
                matrix[r][(c+t) % len(matrix[0])] = 0
                # print("1: ", r, (c+t) % len(matrix[0]))
            for m in range(0, len(matrix)):
                matrix[(r+m) % len(matrix)][c] = 0
                # print("2: ", (r+m) % len(matrix), c)
            
        return matrix