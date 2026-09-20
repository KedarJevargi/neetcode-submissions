class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def solve(word, board, i, j, ci):
            # Bounds check
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            # Character mismatch
            elif word[ci] != board[i][j]:
                return False
            # Word completely matched
            elif ci == len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = '#'  # mark visited

            # Explore all directions
            for move in moves:
                ii, jj = move
                if solve(word, board, i + ii, j + jj, ci + 1):
                    board[i][j] = temp  # restore before returning
                    return True

            board[i][j] = temp  # restore AFTER exploring all directions


        # Try starting from every cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(word, board, i, j, 0):
                    return True
        return False
