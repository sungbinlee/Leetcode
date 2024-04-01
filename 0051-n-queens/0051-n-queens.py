class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 백트래킹으로 완전탐색
        # 수를 둘때마다 가로 세로 대각선 확인
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