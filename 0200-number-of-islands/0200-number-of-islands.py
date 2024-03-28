from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols for _ in range(rows)]
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def is_range(x, y):
            if 0 <= x < rows and 0 <= y < cols:
                return True
            else:
                return False
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            
            while q:
                cur_x, cur_y = q.pop()
                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if is_range(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = True
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
                    
        return cnt