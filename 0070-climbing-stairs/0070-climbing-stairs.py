class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def cs(x):
            if x == 1:
                return 1
            if x == 2:
                return 2
            
            if x not in memo:
                memo[x] = cs(x-1) + cs(x-2)
            
            return memo[x]
        
        return cs(n)