class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        
        def backtrack(i, j, start):
            if start == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[start]:
                return False
            
            tmp, board[i][j] = board[i][j], '#'
            
            for d in range(4):
                if backtrack(i + dx[d], j + dy[d], start + 1):
                    return True
                
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
                
        return False