from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        areas = []
        
        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            q = deque()
            cnt = 1
            q.append((x, y))
            visited[x][y] = True
            
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols:
                        if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                            cnt += 1
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
            return cnt
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    areas.append(bfs(i, j))
        
        return max(areas) if areas else 0
                    