from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 각 정점의 색을 저장할 리스트
        # 0: 아직 색이 칠해지지 않음
        # 1: 그룹 1
        # -1: 그룹 2
        color = [0] * len(graph)
        
        def bfs(start_v):
            q = deque()
            q.append(start_v)
            color[start_v] = 1
            
            while q:
                cur_v = q.popleft()
                for next_v in graph[cur_v]:
                    if color[next_v] == 0:
                        color[next_v] = color[cur_v] * -1
                        q.append(next_v)
                    elif color[next_v] == color[cur_v]:
                        return False
            return True
        
        # 완전탐색 수행
        for start_v in range(len(graph)):
            if color[start_v] == 0:
                if not bfs(start_v):
                    return False
        return True
