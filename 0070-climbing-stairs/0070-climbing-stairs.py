class Solution:
    def climbStairs(self, n: int) -> int:
        
#         memo = {}
        
#         def cs(x):
#             if x == 1:
#                 return 1
#             if x == 2:
#                 return 2
            
#             if x not in memo:
#                 memo[x] = cs(x-1) + cs(x-2)
            
#             return memo[x]
        
#         return cs(n)
        if n == 1:
            return 1
        
        one_before = 1
        two_before = 1
        
        for i in range(2, n+1):
            total = one_before + two_before
            two_before = one_before
            one_before = total
        
        return total