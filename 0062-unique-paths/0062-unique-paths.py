class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] *n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    memo[r][c] = 1
                else:
                    memo[r][c] = memo[r-1][c] + memo [r][c-1]
        
        return memo[-1][-1]
                