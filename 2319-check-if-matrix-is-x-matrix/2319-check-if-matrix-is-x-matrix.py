class Solution:
	def checkXMatrix(self, grid: List[List[int]]) -> bool:
		l = len(grid)
		diagonal, otherElements = True, True
		for i in range(l):
			for j in range(l):
				# print(grid[i][j])
				if (i == j or i + j == l - 1) and (grid[i][j] != 0):
					continue
				elif (i != j or i + j != l - 1) and grid[i][j] != 0:
					# print("Other element and non zero\n")
					otherElements = False
					break
				elif (i == j or i + j == l - 1) and grid[i][j] == 0:
					# print("\nDiagonal and zero\n")
					diagonal = False
					break
				elif (i != j or i + j != l - 1) and grid[i][j] == 0:
					continue
		return (otherElements and diagonal)