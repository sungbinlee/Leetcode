from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(v):
            visited.add(v)
            for next_v in rooms[v]:
                if next_v not in visited:
                    dfs(next_v)
        
        dfs(0)
        
        return len(visited) == len(rooms)
                
        
        