class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def solve(word, board, i, j, ci):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            elif word[ci] != board[i][j]:
                return False

            elif ci == len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = '#'  

     
            for move in moves:
                ii, jj = move
                if solve(word, board, i + ii, j + jj, ci + 1):
                    board[i][j] = temp  
                    return True

            board[i][j] = temp 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(word, board, i, j, 0):
                    return True
        return False
