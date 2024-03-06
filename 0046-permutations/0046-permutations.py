class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            # base case
            if len(nums) == len(curr):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    
        ans = []
        backtrack([])
        return ans
        