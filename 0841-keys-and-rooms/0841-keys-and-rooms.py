from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # DFS 재귀 구현
#         visited = set()
        
#         def dfs(v):
#             visited.add(v)
#             for next_v in rooms[v]:
#                 if next_v not in visited:
#                     dfs(next_v)
        
#         dfs(0)
        
#         return len(visited) == len(rooms)

        # BFS 구현
        visited = [False] * len(rooms)
        
        def bfs(v):
            q = deque()
            q.append(v)
            visited[0] = True
            
            while q:
                cur_v = q.popleft()
                for next_v in rooms[cur_v]:
                    if visited[next_v] == False:
                        q.append(next_v)
                        visited[next_v] = True
        
        bfs(0)
        
        return all(visited)
                
        
        