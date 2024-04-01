from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구현
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))
            
        costs = {}
        pq = []
        heappush(pq, (0, k))

        # 다익스트라 구현
        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heappush(pq, (next_cost, next_node))
            
        # 조건 확인
        print(costs)
        for i in range(1, n+1):
            if i not in costs:
                return -1
        
        # 최대값 반환
        return max(costs.values())