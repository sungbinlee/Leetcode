from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def in_range(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while q:
                cur_x, cur_y = q.popleft()
                for dx, dy in delta:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if in_range(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = True
                        
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    count += 1
        
        return count