class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(x, y, num):
            for i in range(9):
                if board[x][i] == num:
                    return False

            for i in range(9):
                if board[i][y] == num:
                    return False

            start_row, start_col = 3 * (x // 3), 3 * (y // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True
        
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if backtrack():
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False
            return True
        
        backtrack()
