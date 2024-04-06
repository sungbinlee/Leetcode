from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for start_node, end_node, cost in times:
            graph[start_node].append((cost, end_node))
            
        pq = []
        costs = {}
        heappush(pq, (0, k))
        
        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heappush(pq, (next_cost, next_node))
        
        if len(costs) != n:
            return -1
        
        return max(costs.values())