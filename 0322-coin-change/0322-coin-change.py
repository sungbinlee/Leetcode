from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = -1
        depth = 0
        
        visited = set()
        
        q = deque()
        q.append((depth, amount))

        while q:
            curr_depth, curr_amount = q.popleft()
            if curr_amount == 0:
                answer = curr_depth
                break
            for coin in coins:
                next_amount = curr_amount - coin
                if next_amount >= 0 and next_amount not in visited:
                    q.append((curr_depth + 1, next_amount))
                    visited.add(next_amount)
        
        return answer
    
    
    