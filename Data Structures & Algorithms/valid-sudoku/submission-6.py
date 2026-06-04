class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidNine(row: List[str]) -> bool:
            res = [None]*9
            for i in row:
                try:
                    idx = int(i) - 1
                    res[idx] = True if res[idx]==None else False
                except ValueError:
                    pass
            return False not in res

        colValid = squareValid = True
        rowsValid = False not in [isValidNine(i) for i in board]
        
        for i in range(9):
            if not isValidNine([row[i] for row in board]):
                colValid = False
                break
        
        for i in range(9):
            rowStart = (i // 3) * 3
            colStart = (i % 3) * 3
            subGrid = [board[r][colStart : colStart + 3] for r in range(rowStart, rowStart + 3)]
            
            if not isValidNine([cell for row in subGrid for cell in row]):
                squareValid = False
                break
    
        return rowsValid & colValid & squareValid
        