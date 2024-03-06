class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, curr):
            # base case
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for num in range(start, n + 1):
                if num not in curr:
                    curr.append(num)
                    backtrack(num + 1, curr)
                    curr.pop()
            
        ans = []
        backtrack(1, [])
        return ans
            