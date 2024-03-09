class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(x, y):
            # 가로세로
            for i in range(n):
                if board[x][i] == 'Q' or board[i][y] == 'Q':
                    return False
                
            # 대각선 체크 
            for i in range(n):
                for j in range(n):
                    if (i + j == x + y or i - j == x - y) and board[i][j] == 'Q':
                        return False
                    
            return True
                    
        def backtrack(row):
            # base case
            if row == n:
                ans.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
            
        
        board = [['.']*n for _ in range(n)]
        ans = []
        backtrack(0)
        return ans
        
            
            

        