from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        def bfs(start_v):
            q = deque()
            q.append(start_v)
            visited[start_v] = True
            
            while q:
                cur_v = q.popleft()
                for next_v in rooms[cur_v]:
                    if visited[next_v] == False:
                        q.append(next_v)
                        visited[next_v] = True
        
        bfs(0)
        
        return all(visited)