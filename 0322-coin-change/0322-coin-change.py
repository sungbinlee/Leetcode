from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         answer = -1
#         depth = 0
        
#         visited = set()
        
#         q = deque()
#         q.append((amount, depth))
        
#         while q:
#             cur_amount, cur_depth = q.popleft()
#             if cur_amount == 0:
#                 answer = cur_depth
#                 break
#             for coin in coins:
#                 next_amount = cur_amount - coin
#                 if next_amount >= 0 and next_amount not in visited:
#                     q.append((next_amount, cur_depth + 1))
#                     visited.add(next_amount)
                    
#         return answer

        dp = [0] + [float("inf")] * amount
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[-1] == float("inf") else dp[-1]