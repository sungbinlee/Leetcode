class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def combi(tmp, start, target, ans, currSum):
            
            if (currSum == target):
                ans.append(tmp.copy())
                return
            
            for i in range(start, len(candidates)):
                if (i > start and candidates[i] == candidates[i-1]):
                    continue
                if currSum + candidates[i] <= target:
                    tmp.append(candidates[i])
                    combi(tmp, i + 1, target, ans, currSum + candidates[i])
                    tmp.pop()

        combi([], 0, target, ans, 0)
        return ans