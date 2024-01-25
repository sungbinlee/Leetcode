class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        
        
        def dfs(x, y):
            if x == 0 and y == 0:
                memo[x][y] = 1
                return memo[x][y]
            unique_path = 0
            if memo[x][y] == -1:
                if x-1 >= 0:
                    unique_path += dfs(x-1, y)
                if y-1 >= 0:
                    unique_path += dfs(x, y-1)
                memo[x][y] = unique_path

            return memo[x][y]
        
        return dfs(m-1, n-1)