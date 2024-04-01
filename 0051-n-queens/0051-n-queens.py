class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(x, y):
            for i in range(n):
                if board[x][i] == "Q" or board[i][y] == "Q":
                    return False
                
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q" and (i + j == x + y or i - j == x - y):
                        return False
            return True
        
        
        def backtrack(row):
            # basecase
            if row == n:
                answer.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        
        answer = []
        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        
        return answer
        