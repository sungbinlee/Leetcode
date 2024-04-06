from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        m = len(grid)
        visited = [[False] * n for _ in range(m)]
        cnt = 0
        
        def in_range(x, y):
            return 0 <= x < m and 0 <= y < n
        
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited[x][y] = True
            
            while q:
                cur_x, cur_y = q.popleft()
                
                for dx, dy in delta:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if in_range(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = True
        
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        
        return cnt
    