class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSubBoxes(board, r, c):
            temp = []
            for i in range(r[0], r[1]):
                for j in range(c[0], c[1]):
                    if board[i][j] != ".":
                        temp.append(board[i][j])
            return (len(set(temp)) == len(temp))
            
        def checkRows(board, rowNum):
            temp = []
            for i in range(9):
                if board[rowNum][i] != ".":
                    temp.append(board[rowNum][i])
            return (len(set(temp)) == len(temp))
        
        def checkColumns(board, colNum):
            temp = []
            for i in range(0, 9):
                if board[i][colNum] != ".":
                    temp.append(board[i][colNum])
            return (len(set(temp))) == len(temp)
        
        # def main(board):
        for i in range(9):
            res = checkRows(board, i)
            if not res:
                return False
        for j in range(9):
            res = checkColumns(board, j)
            if not res:
                return False

        if not (checkSubBoxes(board, [0,3], [0,3]) and 
                checkSubBoxes(board, [0,3], [3,6]) and 
                checkSubBoxes(board, [0,3], [6,9]) and 
                checkSubBoxes(board, [3,6], [0,3]) and 
                checkSubBoxes(board, [3,6], [3,6]) and
                checkSubBoxes(board, [3,6], [6,9]) and 
                checkSubBoxes(board, [6,9], [0,3]) and
                checkSubBoxes(board, [6,9], [3,6]) and 
                checkSubBoxes(board, [6,9], [6,9])):
            return False
        return True

        # main(board)