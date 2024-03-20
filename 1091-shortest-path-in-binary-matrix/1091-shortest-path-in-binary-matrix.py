from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_path = -1
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return shortest_path
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        while q:
            cur_x, cur_y, cur_len = q.popleft()
            
            if cur_x == rows - 1 and cur_y == cols - 1:
                shortest_path = cur_len
                break
                
            for dx, dy in delta:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        q.append((next_x, next_y, cur_len + 1))
                        visited[next_x][next_y] = True
                
        
        return shortest_path