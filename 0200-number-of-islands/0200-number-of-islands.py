from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        
        def bfs(x, y):
            visited[x][y] = True
            q = deque()
            q.append((x, y))
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            while q:
                curr_x, curr_y = q.popleft()
                for i in range(4):
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    count += 1
            
        return count
