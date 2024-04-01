from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def in_range(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid)
        
        
        def bfs(x, y):
            q = deque()
            q.append((x, y, 1))
            
            delta = [(1, 0), (0, 1), (0, -1), (-1, 0),
                    (1, 1), (-1, -1), (-1, 1), (1, -1)]
            
            visited = [[False] * len(grid) for _ in range(len(grid))]
            visited[x][y] == True
            
            while q:
                cur_x, cur_y, cur_d = q.popleft()
                if cur_x == len(grid) - 1 and cur_y == len(grid) - 1:
                        return cur_d
                    
                for dx, dy in delta:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if in_range(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                        q.append((next_x, next_y, cur_d + 1))
                        visited[next_x][next_y] = True
            return -1
        
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        return bfs(0, 0)
        
        
        