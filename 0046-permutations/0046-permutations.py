class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr):
            if len(nums) == len(curr):
                answer.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()     
        
        answer = []
        backtrack([])
        return answer