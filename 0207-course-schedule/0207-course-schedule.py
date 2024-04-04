from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 위상 정렬로
        visited = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)
        
        while q:
            cur_v = q.popleft()
            visited.append(cur_v)
            
            for next_v in graph[cur_v]:
                indegree[next_v] -= 1
                
                if indegree[next_v] == 0:
                    q.append(next_v)
        
        if len(visited) == numCourses:
            return True
        return False
        
        