from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        pq = []
        probabilities = [0] * n
        
        heappush(pq, (-1, start_node))
        
        while pq:
            cur_prob, cur_node = heappop(pq)
            cur_prob *= -1
            
            if probabilities[cur_node] >= cur_prob:
                continue
                
            probabilities[cur_node] = cur_prob
            
            if cur_node == end_node:
                return cur_prob
            
            for next_node, prob in graph[cur_node]:
                next_prob = prob * cur_prob
                if next_prob >= probabilities[next_node]:
                    heappush(pq, (-next_prob, next_node))
                    
        return 0
