from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구현
        graph = defaultdict(list)
        for start_v, end_v, cost in times:
            graph[start_v].append((cost, end_v))
        
        # 다익스트라
        pq = []
        costs = {}
        heappush(pq, (0, k))
        
        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cost + cur_cost
                    heappush(pq, (next_cost, next_node))
        # 비교
        for i in range(1, n+1):
            if i not in costs:
                return -1
        
        # 최대값 반환
        return max(costs.values())