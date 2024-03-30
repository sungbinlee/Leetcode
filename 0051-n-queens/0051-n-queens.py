class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 백트래킹으로 완전탐색
        # - 한줄당 하나씩 
        # 수를 둘때마다 대각선 및 가로 확인
        def is_valid(x, y):
            # 가로 세로 확인
            for i in range(n):
                if board[x][i] == "Q" or board[i][y] == "Q":
                    return False
                
            # 대각선 확인
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q" and (i + j == x + y or i - j == x - y):
                        return False
                    
            return True
        
        
        def backtrack(row):
            # basecase
            if row == n:
                ans.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
            
        
        board = [["."] * n for _ in range(n)]
        ans = []
        backtrack(0)

        
        return ans
        