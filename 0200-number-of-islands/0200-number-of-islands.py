from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = [[False] * columns for _ in range(rows)]
        q = deque()
        
        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            q.append((x, y))
            visited[x][y] = True
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < columns:
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
            
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and not visited[i][j]: 
                    bfs(i, j)
                    count += 1
                
            
        return count
