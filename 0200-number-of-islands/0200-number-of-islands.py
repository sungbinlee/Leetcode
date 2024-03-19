from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        
        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols:
                        if not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and not visited[x][y]:
                    bfs(x, y)
                    cnt += 1
        
        return cnt