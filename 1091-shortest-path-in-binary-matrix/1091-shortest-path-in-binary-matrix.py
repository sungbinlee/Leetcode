from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 좌상단 우하단으로 이동해야함
        # 대각선으로 이동가능
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def bfs():
            q = deque()
            visited = [[False] * cols for _ in range(rows)]
            q.append((0, 0, 1))
            visited[0][0] = True

            delta = [(1, 0), (0, 1), (-1, 0), (0, -1),
                    (1, 1), (-1, 1), (-1, -1), (1, -1)]
            
            while q:
 
                cur_x, cur_y, cur_d = q.popleft()
                if cur_x == rows-1 and cur_y == cols-1:
                    return cur_d
                for dx, dy in delta:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if is_valid(next_x, next_y) and grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        q.append((next_x, next_y, cur_d + 1))
                        visited[next_x][next_y] = True
            
            return -1

        answer = bfs()
        
        return answer