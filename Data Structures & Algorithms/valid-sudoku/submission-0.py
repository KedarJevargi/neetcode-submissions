class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(board) -> bool:
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] != ".":
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
            return True

        def check_column(board) -> bool:
            for j in range(9):
                seen = set()
                for i in range(9):
                    if board[i][j] != ".":
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
            return True

        def check_sub(board, row, col) -> bool:
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = board[row + i][col + j]
                    if val != ".":
                        if val in seen:
                            return False
                        seen.add(val)
            return True

   
        if not check_row(board):
            return False

   
        if not check_column(board):
            return False

 
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_sub(board, i, j):
                    return False

        return True
