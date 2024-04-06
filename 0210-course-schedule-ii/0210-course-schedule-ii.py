from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False] * numCourses
        graph = defaultdict(list)
        answer = []
        indegree = [0] * numCourses
        
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)
        temp = []
        
        while q:
            cur_course = q.popleft()
            visited[cur_course] = True
            temp.append(cur_course)
            
            for next_v in graph[cur_course]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    q.append(next_v)
        
        if len(temp) == numCourses:
            answer = temp
        
        return answer
        